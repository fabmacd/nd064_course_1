from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK - health"}),
        status=200,
        mimetype='application/json'
    )
    ## log line status
    app.logger.info('status request successful')
    
    return response
    
@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    ## log line metrics
    app.logger.info('Metrics request successful')
    
    return response

@app.route("/")
def hello():
    ## log line main
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
