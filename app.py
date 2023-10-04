import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  app.app_context().push()
  setup_db(app)
  CORS(app)

  @app.route("/movies")
  @requires_auth('get:movies')
  def get_movies(payload):
      movies = Movies.query.order_by(Movies.id).all()
      movies_dic= {}  
    
      for movie in movies:
          movies_dic[movie.id] = Movies.format(movie)

      try:
            return jsonify(
                {
                    "success": True,
                    "movies": movies_dic,
                    "total_movies": len(Movies.query.all()),
                }
            )
      except AuthError as e:
         abort(e.status_code)
      except:
          abort(422)

  @app.route("/movies/<int:movie_id>")
  @requires_auth('get:movies')
  def retreive_movies_by_id(payload,movie_id):
        try:
            movie = Movies.query.filter(Movies.id==movie_id).one_or_none()            
            if movie is None:
                abort(404)
            
            return jsonify(
                {
                    "success": True,
                    "movie": Movies.format(movie),
                }
            )
        except AuthError as e:
            abort(e.status_code)
        except:
            abort(422)          

  @app.route("/movie", methods=["POST"])
  @requires_auth('post:movie')
  def create_movie(payload):
        body = request.get_json()

        new_title = body.get("title")
        new_releaseDate = body.get("releaseDate")

        try:
            movie = Movies(title=new_title,release_date=new_releaseDate)
            movie.insert()

            return jsonify(
                {
                    "success": True,
                    "created": movie.id
                }
            )
        except AuthError as e:
            abort(e.status_code)
        except:
            abort(422)

  @app.route("/movies/<int:movie_id>", methods=["PATCH"])
  @requires_auth('patch:movie')
  def update_movie(payload,movie_id):
    
    body = request.get_json()
    new_title = body.get("title")
    new_releaseDate = body.get("releaseDate")

    try:
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        if new_title is not None:
            if new_title != movie.title:
               movie.title = new_title

        if new_releaseDate is not None:
            if new_releaseDate != movie.release_date:
               movie.release_date = new_releaseDate  

        movie.update()

        updated_movie = Movies.query.get(movie_id)
        movies = Movies.format(updated_movie)
        
        return jsonify(
                {
                    "success": True,
                "movie": movies,
                }
            )
    except AuthError as e:
            abort(e.status_code)
    except:
            abort(422)         

  @app.route("/movies/<int:movie_id>", methods=["DELETE"])
  @requires_auth('delete:movie')
  def delete_movie(payload,movie_id):
        try:    
            movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": movie_id,
                    "total_movies": len(Movies.query.all()),
                }
            )
        except AuthError as e:
            abort(e.status_code)
        except:
            abort(422)        
  
  
  @app.route("/actors")
  @requires_auth('get:actors')
  def get_actors(payload):
      actors = Actors.query.order_by(Actors.id).all()
      actors_dic= {}  
    
      for actor in actors:
          actors_dic[actor.id] = Actors.format(actor)

      try:
            return jsonify(
                {
                    "success": True,
                    "actors": actors_dic,
                    "total_actors": len(Actors.query.all()),
                }
            )
      except AuthError as e:
            abort(e.status_code)
      except:
            abort(422)

  @app.route("/actors/<int:actor_id>")
  @requires_auth('get:actors')
  def retreive_actors_by_id(payload,actor_id):
        try:
            actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
            
            if actor is None:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "actor": Actors.formatSingleActor(actor),
                }
            )
        except AuthError as e:
            abort(e.status_code)
        except:
            abort(422)           

  
  @app.route("/actor", methods=["POST"])
  @requires_auth('post:actor')
  def create_actors(payload):
        body = request.get_json()

        new_name = body.get("name")
        new_age = body.get("age")
        new_gender= body.get("gender")
        new_movie_id= body.get("movie_id")

        try:
            actor = Actors(name=new_name,age=new_age,gender=new_gender,movie_id=new_movie_id)
            actor.insert()

            return jsonify(
                {
                    "success": True,
                    "created": actor.id
                }
            )
        except AuthError as e:
            abort(e.status_code)
        except:
            abort(422)

  @app.route("/actor/<int:actor_id>", methods=["PATCH"])
  @requires_auth('patch:actor')
  def update_actor(payload,actor_id):
    
    body = request.get_json()
    new_name = body.get("name")
    new_age = body.get("age")
    new_gender = body.get("gender")
    new_movie_id = body.get("movie_id")

    try:
        actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        if new_name is not None:
            if new_name != actor.name:
               actor.name = new_name

        if new_age is not None:
            if new_age != actor.age:
               actor.age = new_age

        if new_gender is not None:
            if new_gender != actor.gender:
               actor.gender = new_gender 

        if new_movie_id is not None:
            if new_movie_id != actor.movie_id:
               actor.movie_id = new_movie_id       

        actor.update()

        updated_actor = Actors.query.get(actor_id)
        
        return jsonify(
                {
                "success": True,
                "actor": Actors.format(updated_actor),
                }
            )
    except AuthError as e:
            abort(e.status_code)
    except:
            abort(422)          

  @app.route("/actors/<int:actor_id>", methods=["DELETE"])
  @requires_auth('delete:actor')
  def delete_actor(payload,actor_id):
        try:    
            actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": actor_id,
                    "total_actors": len(Actors.query.all()),
                }
            )
        except AuthError as e:
            abort(e.status_code)
        except:
            abort(422)  

  @app.errorhandler(404)
  def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

  @app.errorhandler(422)
  def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

  @app.errorhandler(400)
  def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400
    
  @app.errorhandler(405)
  def method_not_allowed_request(error):
        return jsonify({"success": False, "error": 405, "message": "The method is not allowed for the requested URL."}), 405

  @app.errorhandler(500)
  def bad_request(error):
        return jsonify({"success": False, "error": 500, "message": "internal server error"}), 500  

  @app.errorhandler(AuthError)
  def autherror_handler(ex):
    return jsonify({
        "success": False,
        "error": ex.status_code,
        "message": ex.error["description"]
    }), ex.status_code                 

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)