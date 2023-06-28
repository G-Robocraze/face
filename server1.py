from crypt import methods
from glob import glob
from flask import Flask,jsonify


def start_server(emotions:list,host:str,port:int,callback):
    app = Flask(__name__)


    @app.route("/1",methods=["GET"])
    def emotion1():
        current_emotion = emotions[0]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/2",methods=["GET"])
    def emotion2():
        current_emotion = emotions[1]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/3",methods=["GET"])
    def emotion3():
        current_emotion = emotions[2]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/4",methods=["GET"])
    def emotion4():
        current_emotion = emotions[3]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/5",methods=["GET"])
    def emotion5():
        current_emotion = emotions[4]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/6",methods=["GET"])
    def emotion6():
        current_emotion = emotions[5]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/7",methods=["GET"])
    def emotion7():
        current_emotion = emotions[6]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/8",methods=["GET"])
    def emotion8():
        current_emotion = emotions[7]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    @app.route("/9",methods=["GET"])
    def emotion9():
        current_emotion = emotions[8]
        callback(current_emotion)
        return jsonify({"status": True,"emotion":current_emotion})

    app.run(host=host,debug=False,port=port)
