from flask import Blueprint, request, jsonify
from usecases import use_cases_client
from entities.model import Client
import logging

client_bp=Blueprint("client_bp", __name__)

request_mapping="/client"


@client_bp.route(request_mapping, methods=["POST"])
def insert():
    json=request.get_json()
    if not json:
        logging.warning("empty body insert")
        return {"message": "empty body"}, 400
    try:
        if use_cases_client.insert(Client(**json)):
            logging.info("OK INSERT")
            return {"message": "inserted"}, 201
    except Exception as ex:
        logging.error("ERROR INSTERT: {%s}", ex)

    return {"mesage": "server error"}, 500

@client_bp.route(request_mapping, methods=["GET"])
def select():
    try:
        data = use_cases_client.select_all()
        if data:
            print(data)
            dictionary = [{"id": t.id, "name":t.name, "address": t.address, "email": t.email} for t in data]
            logging.info("OK GET ALL")
            return {"result": dictionary}, 200
    except Exception as ex:
        logging.error("ERROR GET ALL CLIENTS: {%s}", ex)

    return {"message": "server error"}, 500

@client_bp.route(request_mapping, methods=["DELETE"])
def delete():
    id=request.args["id"]
    if not id:
        logging.warning("QUERY PARAMETER ID DOESN´T EXIST DELETE")
        return {"message": "must be exist query parameter id"}, 400
    try:
        if use_cases_client.delete_by_id(id):
            logging.info("DELETED OK")
            return {"message": "OK DELETED"}, 200
        else:
            logging.info("ID {%s} DOESN´T EXIST DELETE", id)
            return {"message": f"client id {id} doesn´t exist"}, 404
        
    except Exception as ex:
        logging.error("ERROR DELETE: {%s}", ex)
        

    return {"message": "server error"}, 500

@client_bp.route(request_mapping, methods=["PUT"])
def update():
    data = request.get_json



    if not data:
        logging.warning("body empty update")
        return {"message": "empty body"}, 400
    try:
        if use_cases_client.update(Client(**data)):
            logging.info("UPDATE OK")
            return {"message": "OK"}, 200
        else:
            logging.info("CLIENT {%s} DOESN´T EXIST", id)
            return {"message": f"client id {id} doesn´t exist"}, 404
        
    except Exception as ex:
        logging.error("ERROR UPDATE: {%s}", ex)
        

    return {"message": "server error"}, 500


