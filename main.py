from flask import Flask, jsonify, request, redirect, url_for 
from bson import ObjectId 
from pymongo import MongoClient  
import os  
import requests
    
app = Flask(__name__)  


global server
server = os.environ.get('SERVER')

if (server == None):
    print("env variable server must be set to VPN database endpoint")
    exit()

    
def redirect_url():  
    return request.args.get('next') or request.referrer or url_for('index')  
     


@app.route("/todo", methods=['POST'])  
def post_todo ():  
    global server 
    title=request.values.get("title")  
    desc=request.values.get("description")  

    data = {"title": title, "description": desc}
    r = requests.post(url = server + "/todo", data = data)  
    return jsonify({'status' : 'success', 'data' : r.json()['data']})    

@app.route("/todo", methods=['GET'])  
def get_todo():  
    global server

    r = requests.get(url = server + "/todo")
    print(r.json())  
    return jsonify({'status' : 'success', 'data' : r.json()['data']}) 

@app.route("/todo", methods=['DELETE'])  
def delete_todo():  
    global server
    title=request.values.get("title")
    url = server + "/todo/" + title
    print(url)
    r = requests.delete(url = url)

    return jsonify({'status' : 'success', 'data' : r.json()['data']}) 
    



if __name__ == "__main__":  
    
    app.run(host = "0.0.0.0")