#!flask/bin/python
from flask import Flask
import json
import picamera
import random
import os.path
import time

app = Flask(__name__)


if not (os.path.exists("counter.txt")):
    print "Initializing file counter"
    counterFile = open("counter.txt", "w")
    counterFile.write("0")
    counterFile.close()

counterFile = open("counter.txt", "r+")
ct = int(counterFile.read())
print "File Counter: " + str(ct)
counterFile.seek(0)

dummyResposne ={"module":"camera","timestamp":1486836445,"file_name":"file_300795","file_extension":"jpeg"}

@app.route('/')
def index():
    return "Traffic Violation Detector Camera Module"

@app.route('/trigger-camera')
def cameraTrigger():
    camera = picamera.PiCamera()
    camera.hflip = True
    camera.vflip = True
    count = counterFile.read();
    fileName = "file_" + count
    camera.capture(fileName + ".jpg")
    timestamp = time.time()
    response = {}
    response["module"] = "camera"
    response["timestamp"] = timestamp
    response["file_name"] = fileName
    response["file_extension"] = "jpg"
    
    counterFile.seek(0)
    counterFile.write(str(int(count) + 1))
    counterFile.seek(0)
    camera.close()
    return json.dumps(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=3001)
