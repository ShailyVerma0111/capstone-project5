# Capstone

### Motivation
In this final project of fullstack nanodegree program, i have implemeted all the learning we did as part of this program in movie application, from database setup to building apis to authenticating =users and adding role based permissions and deploying the application on render. This has given me lot of confident on my learning journey so far. 
In this movie application I have created ten endpoints in total, five for movie CRUD operations and five for actor CRUD operations.
There are three roles defined as part of this application:
-Casting Assitant
-Casting Director
-Executive Producer

Rolebased permissions has been defined for all three users in Auth0.

## Project Repository

The project repository with latest code for this application is `https://github.com/ShailyVerma0111/capstone-project5`

### Install Dependencies
install the required dependencies using below command:

```bash
pip install -r requirements.txt
```

### Set up the Database

With Postgres running, create a `capstone` database:

```bash
createdb capstone
```

Populate the database using the `capstone.psql` file provided. In terminal run:

```bash
psql capstone < capstone.psql
```

### Tests
In order to run tests navigate to project folder and run the following commands: 

```
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone.psql
python test_app.py
```

The first time you run the tests, omit the dropdb command.

## API Reference

### Getting Started
- Base URL: At present the application is hosted on render `https://capstone-app-deployment.onrender.com` and in local runs on `http://127.0.0.1:8080/`,
- Authentication: This version of the application is using Auth0 as third party authentication and will require below bearer tokens for authentication. 

#### Role: Executive Producer
##### bearer token: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFTWWlmZlg1SWNzbnZ1MllUNTNaaCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZS1jYWZlLXNob3AudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY1MTMwYWFiMjA1ZTBmNjQwMWU0Yjc3YiIsImF1ZCI6IkNhcFN0b25lIiwiaWF0IjoxNjk2NTA4MjI0LCJleHAiOjE2OTY1OTQ2MjQsImF6cCI6IlFmSml6TmxWQkFERHlweFR4ampkTm9BdER1ckZhQ3BDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.fQq2cwaoVun0eEtxqbYfdSsPTMmkAYFXs3w-hPR-ir_1xqQIJRE8xEx86L2qNYYVQh1lQViBS2dnJAc1Pa7Ii0sukZCayfdN2wuxgPlPfb6lvS_SkjMRkTIwlIV_fnPqq5-ypiSqk0mvTxSjUsYKWSkvv2J92hP6u4xpEU4NHY5aew9X349ndU2JB_ReFkRMKEKYhzIggqGi33aANa6UJ0SBoJWTfNw1hYncJA78htRJ7wTmzQfQ_M29usQ7c5MFTTtWNrAeSlwUKzzS4bSx0OFUL1KiS0eba51OtOVtvhbVxKl_D6phe4v-XLu6wic9s5rxwcWrU16Ef0jouqsA-g

#### Role: Casting Assitant
##### bearer token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFTWWlmZlg1SWNzbnZ1MllUNTNaaCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZS1jYWZlLXNob3AudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0ZDMzNDYwN2YxODQ1MGRjMjRlYWM4NyIsImF1ZCI6IkNhcFN0b25lIiwiaWF0IjoxNjk2NTIwNjM2LCJleHAiOjE2OTY2MDcwMzYsImF6cCI6IlFmSml6TmxWQkFERHlweFR4ampkTm9BdER1ckZhQ3BDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.K48vrwghy6d1dUQWv3O5Q1fuzOvuFhKT-X7l2SlBPhuVs1CHabWPSYopINqvehDaz2tQP6yz68RYRspwBVWKZpgtTRqYJ9TQDx826SWLIk4VODqezuhHKjNdDWh0cs-TamptXCAWgEyUXBKWORupydrafUMki05inKYxdsyYprK3awNU3kng3j3XzdjhCa63aG_JMFUD1eUBRLgi_l0v4S4yQF2otTt9Lr8ZMH6Q6s0EhTj0G66-mszHK1qLIh687T3T_plZ7tlj0AQnb0Lmpvp1T9cryn8ZAJR4MkiX6pL_Eabfq1WrGyNWi31Jxqp_iR6tlzzUA1sVxQWmwVMAEg

#### Role: Casting Director
##### bearer token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFTWWlmZlg1SWNzbnZ1MllUNTNaaCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZS1jYWZlLXNob3AudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0ZDM0OTk3N2YxODQ1MGRjMjRlYWY5YiIsImF1ZCI6IkNhcFN0b25lIiwiaWF0IjoxNjk2NTE5MjUzLCJleHAiOjE2OTY2MDU2NTMsImF6cCI6IlFmSml6TmxWQkFERHlweFR4ampkTm9BdER1ckZhQ3BDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIl19.m7NIcXCrEisrtjX50TF8SD3CrtEIPFGpbOERCdmks3337AqIMO2PSJKxyxVleBUVeoBwDJf0PL-1mlzUdFx7_BmdOfTnXrS187zAV6XtSgJAM5_qKK3-RvW429IaqKzFlhxiDAntfm8O-TncXc_0f80nIfW43FsEiJRiVpjCHPIr0aJWVfyS_z3xxwvMcFG0OodPB7qMprdkAenO3bbJNuTZUlkQxoK9-nW7YLzsNWaKZv9_CJP2pnWizPlp1HSX6S6d_aPDnTzslFiw2vJTjVyPKLeU0dW89ehm7rWDEgeU0JUNMw7NSJY6tDoMG9eePqhZA7_0JjocQgzedud3MQ


### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal server error
- 401: UNAUTHORIZED
- 403: Permission not found.

### Endpoints 
#### GET /movies
- General:
    - Returns a list of movies, success value, and total number of movies 
- Sample: `curl http://127.0.0.1:8080/movies`

``` 
{
    "movies": {
        "1": {
            "release_date": "20-09-2001",
            "title": "Forest Gump"
        },
        "2": {
            "release_date": "21-09-2003",
            "title": "Pursuit of Happiness"
        },
        "3": {
            "release_date": "23-09-2005",
            "title": "Jab we met"
        },
        "4": {
            "release_date": "23-09-2006",
            "title": "Sultan"
        }
    },
    "success": true,
    "total_movies": 4
}
```

#### GET /movies/<int:movie_id>
- General:
    - Returns a list of movie objects and success value 
- Sample: `curl http://127.0.0.1:8080/movies/2`

``` 
{
    "movie": {
        "release_date": "21-09-2003",
        "title": "Pursuit of Happiness"
    },
    "success": true
}
```

#### GET /actors
- General:
    - Returns a list of actors objects, success value and total number of actors 
- Sample: `curl http://127.0.0.1:8080/actors`

``` 
{
    "actors": {
        "1": {
            "age": 45,
            "gender": "Male",
            "movie_id": 3,
            "name": "Shahid Kapoor"
        },
        "2": {
            "age": 65,
            "gender": "Male",
            "movie_id": 1,
            "name": "Tom Hanks"
        },
        "3": {
            "age": 60,
            "gender": "Male",
            "movie_id": 2,
            "name": "Will Smith"
        },
        "4": {
            "age": 60,
            "gender": "Male",
            "movie_id": 4,
            "name": "Salman Khan"
        }
    },
    "success": true,
    "total_actors": 4
}
```

#### GET /actors/<int:actor_id>
- General:
    - Returns a list of actors objects and success value 
- Sample: `curl http://127.0.0.1:8080/actors/1`

``` 
{
    "actor": {
        "age": 45,
        "gender": "Male",
        "id": 1,
        "name": "Shahid Kapoor"
    },
    "success": true
}
```

#### POST /actor
- General:
    - Creates a new actor. Returns the id of the created actor and success value. 
- `curl -X POST -H "Content-Type: application/json" -d '{"name": "Tom Cruise", "age": "70", "gender": "Male", "movie_id": 1}' http://127.0.0.1:8080/actor`
```
{
    "created": 24,
    "success": true
}
```

#### POST /movie
- General:
    - Creates a new movie. Returns the id of the created movie and success value. 
- `curl -X POST -H "Content-Type: application/json" -d '{"title": "Hangover", "releaseDate": "01-03-2004"}' http://127.0.0.1:8080/movie`
```
{
    "created": 7,
    "success": true
}
```

#### PATCH /actor
- General:
    - Updated an existing actor. Returns the actor details and success value. 
- `curl -X PATCH -H "Content-Type: application/json" -d '{"name": "shahid kapoor", "age": "70", "gender": "Male","movie_id":"3"}' http://127.0.0.1:8080/actor/1`
```
{
    "actor": {
        "age": 70,
        "gender": "Male",
        "movie_id": 3,
        "name": "Shahid Kapoor"
    },
    "success": true
}
```

#### PATCH /movie
- General:
    - Updated and existing movie. Returns the movie details and success value. 
- `curl -X PATCH -H "Content-Type: application/json" -d '{"title": "Jab We Met Return", "releaseDate": "12-09-2021"}' http://127.0.0.1:8080/movies/3`
```
{
    "movie": {
        "release_date": "12-09-2021",
        "title": "Jab We Met Return"
    },
    "success": true
}
```

#### DELETE /actors/<int:actor_id>
- General:
    - Deletes the actor of the given ID if it exists. Returns the id of the deleted actor, success value and total actors. 
- `curl -X DELETE http://127.0.0.1:8080/actors/1`
```
{
    "deleted": 1,
    "success": true,
    "total_actors": 4
}
```

#### DELETE /movies/<int:movie_id>
- General:
    - Deletes the movie of the given ID if it exists. Returns the id of the deleted movie, success value and total movies. 
- `curl -X DELETE http://127.0.0.1:8080/movies/1`
```
{
    "deleted": 1,
    "success": true,
    "total_movies": 4
}
```
### Testing
I have written unit test for all the endpoints ofr both success and failure scenarios in test_app.py file.
I have tested RBAC control for all three roles using postman by passing bearer tokens for all end points.

## Acknowledgements 
Had great fun developing this project, thanks to whole team of udacity for amazing course! 

