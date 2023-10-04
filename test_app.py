
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from models import setup_db, Movies, Actors
from app import create_app

class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        #binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {"title": "Hangover", "releaseDate": "12-09-2022"}
        self.update_movie = {"title": "Jab We Met Return", "releaseDate": "12-09-2021"}
        self.new_actor = {"name": "Aishwarya Rai", "age": "45", "gender": "female", "movie_id":"3"}  
        self.update_actor = {"name": "Shahid Kapoor", "age": "70", "gender": "Male", "movie_id": "3"}

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"]) 
        self.assertTrue(data["total_movies"])     

    def test_delete_movie(self):
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        movies = Movies.query.filter(Movies.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_movies'])
        self.assertEqual(movies, None)  

    def test_422_when_movie_id_does_not_exist_to_delete(self):
        res = self.client().delete('/movies/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")            
       
    def test_get_movies_by_id(self):
        res = self.client().get("/movies/2")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])

    def test_422_when_actor_id_does_not_exist(self):
        res = self.client().get("/movies/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_create_new_movie(self):
        res = self.client().post("/movie", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])

    def test_405_if_movie_creation_not_allowed(self):
        res = self.client().post("/movies/100", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "The method is not allowed for the requested URL.") 

    def test_404_if_movie_creation_not_allowed(self):
        res = self.client().post("/movie/100", json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_update_movie(self):
        res = self.client().patch("/movies/3", json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_if_movie_update_not_allowed(self):
        res = self.client().patch("/movies/100", json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_get_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"]) 
        self.assertTrue(data["total_actors"])     

    def test_delete_actor(self):
        res = self.client().delete('/actors/4')
        data = json.loads(res.data)

        actor = Actors.query.filter(Actors.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 4)
        self.assertTrue(data['total_actors'])
        self.assertEqual(actor, None)  

    def test_422_when_actor_id_does_not_exist_to_delete(self):
        res = self.client().delete('/actors/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")            
       
    def test_get_actor_by_actorId(self):
        res = self.client().get("/actors/1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_422_when_actor_id_does_not_exist(self):
        res = self.client().get("/actors/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_create_new_actor(self):
        res = self.client().post("/actor", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])

    def test_405_if_actor_creation_method_not_allowed(self):
        res = self.client().post("/actors", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "The method is not allowed for the requested URL.") 

    def test_404_if_actor_creation_not_allowed(self):
        res = self.client().post("/actors/100/", json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_update_actor(self):
        res = self.client().patch("/actor/1", json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_if_actor_update_not_allowed(self):
        res = self.client().patch("/actor/100", json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")     


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()