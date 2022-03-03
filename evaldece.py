from flask import Flask, request, jsonify, redirect, url_for
from flask_pymongo import PyMongo
import pymongo
import requests
from logging import log
#initialisation du server flask
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Decepticon"
mongo = PyMongo(app)

@app.route('/postdata', methods=['POST'])
def create_users():
    currentCollection = mongo.db.Decepticon
    index = request.json['index']
    Decepticon = request.json['Decepticon']
    currentCollection.insert_one({'index' : index,'Decepticon' : Decepticon})
    return jsonify({'index' : index, 'Decepticon' : Decepticon})
#methode get
@app.route('/getall', methods=['GET'])
def getAll():
    board = list()
    currentCollection = mongo.db.Decepticon
    for i in currentCollection.find():
        board.append({'index' : i['index'],'Decepticon' : i['Decepticon']})
    return jsonify(board)


@app.route('/getall/<Decepticon>', methods=['GET'])
def get_name(Decepticon):
    currentCollection = mongo.db.Decepticon
    data = currentCollection.find_one({"Decepticon" : Decepticon})
    return jsonify({'index' : data['index'],'Decepticon' : data['Decepticon']})

@app.route('/deletedata/<Decepticon>', methods=['DELETE'])
def delete_data(Decepticon):
    currentCollection = mongo.db.Decepticon
    currentCollection.delete_one({'Decepticon' : Decepticon})
    return redirect(url_for('getAll')) 

@app.route('/updatedata/<Decepticon>', methods=['PUT'])
def update_data(Decepticon):
    currentCollection = mongo.db.Decepticon
    updateIndex = request.json['index']
    updateDecepticon = request.json['Decepticon']
    currentCollection.find_one({'Decepticon' : Decepticon})
    currentCollection.update_many({'Decepticon' : Decepticon}, {"$set" : { 'index' : updateIndex,'Decepticon' : updateDecepticon}})
    return jsonify({'index' : updateIndex, 'Decepticon' : updateDecepticon})

@app.route('/getall/pagination/', methods=['GET'])
def pagination():
    collectionData = mongo.db.Decepticon
    pageNumber = int(request.args['PageNumber'])
    limit = int(request.args['limit'])
    starting_id = collectionData.find().sort('_id', pymongo.ASCENDING)
    last_id = starting_id[pageNumber]['_id']
    query = collectionData.find({'_id' : {'$gte' : last_id}}).sort('_id', pymongo.ASCENDING).limit(limit)
    print(query[0])
    output = []
    for i in query:
        output.append({'collectionData': i})
    return jsonify({'result' : str(output), 'prev_url' : '', 'next_url' : ''})
if __name__ == "__main__":
    app.run(debug=True)