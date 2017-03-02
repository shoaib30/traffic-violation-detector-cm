#!flask/bin/python
from flask import Flask
import json
app = Flask(__name__)
dummyResposne ={"module":"camera","timestamp":1486836445,"file_name":"file_300795","file_extension":"jpeg"}
@app.route('/')
def index():
    return "Traffic Violation Detector Camera Module"

@app.route('/trigger-camera')
def cameraTrigger():
    return json.dumps(dummyResposne), 200

if __name__ == '__main__':
    app.run(debug=True, port=3001)
