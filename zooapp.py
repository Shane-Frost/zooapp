
#importing flask, cause you need flask to host the web server thingy. 
# see https://flask.palletsprojects.com/en/2.0.x/quickstart/
from flask import Flask, request,Response
import json
app = Flask(__name__)

#Placeholder for a temporary database until we're learned how to do it.
zoo_animals = {
    "1": {"Animal": "Lion", "Age": "11", "Country": "South Africa"},
    "2": {"Animal": "tiger", "Age": "13", "Country": "India"},
}


@app.route("/")
def hello_world():
    return "WELCOME TO MY ZOO"


@app.route("/zoo", methods=["GET"])
def get_zoo_animals():
    return json.dumps(zoo_animals)

# #CREATE, "POST"
# @app.route("/zoo/add", methods=["POST"])
# def add_zoo():
#     Age = request.args.get('Age')
#     Animal = request.args.get('Animal')
#     Country = request.args.get('Country')
#     id = len(zoo_animals) + 1
#     zoo_animals[id] = {"Age": str(Age), "Animal": str(Animal), "Country": str(Country)}
#     return zoo_animals[id]

#Create - From Movie
@app.route("/zoo/add", methods=['POST'])
def add_animal():
    req_data = request.get_json()
    print('data', req_data)
    animal = req_data['Animal']
    age = req_data['Age']
    country = req_data['Country']
    id = str(len(zoo_animals) + 1)
    new_animal = { id : { 'Animal': animal, 'Age': age, 'Country': country } }
    zoo_animals.update(new_animal)
    return f"Animal Added to the Zoo, {json.dumps(zoo_animals)}"


# READ

# http://127.0.0.1:5000/zoo/?id=1
# pass a query parameter (stuff that comes after the ?) which you can then access via request.args.get
# the use the query parameter (id) to do your logic zoo_animals[id]
@app.route("/zoo/", methods=["GET"])#Get is always get, you didn't create this, this is inbuilt in python/flask/restAPI.
def get_an_animal():#DEF = you are defining a function, so it always must be "def function_name()" which is then followed by the function functionality :D" etc.
    id = request.args.get('id')
    return json.dumps(zoo_animals[id])





# DELETE
@app.route("/zoo/delete", methods=["DELETE"])
def delete_animal():
    delete_animal_id = request.args.get('id')
    del zoo_animals[delete_animal_id]
    return "Animal " + delete_animal_id + " is dead"



if __name__ == "__main__":
    app.run(host='127.0.0.1')

    #curl -X POST http://127.0.0.1:5000/zoo/add -d '{"Animal": "Tortoise, "Age": "200", "Country": "Canada"}' -H 'Content-Type: application/json'
