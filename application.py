from flask import Flask,request,app
from flask import Response
from flask_cors import CORS
from lr_deploy import predobj

application = Flask(__name__) #initialising the flask app
app = application
CORS(app)
app.config['debug'] = True

class ClientApi:

    def __init__(self):
        self.predobj = predobj()

@app.route("/predict", method = ['POST'])

def predict_route():
    try:
        if request.json['data']is not None:
            data = request.json['data']
            print('data is: ', data)
            pred = predobj()
            res = pred.predict_log(data)
            print('result is: ', res)
            return Response(res)

    except ValueError:
        return Response('value not found')
    except Exception as e:
        print("exception: ",e)
        return Response(e)

if __name__ == "__main__":
    clntApp = ClientApi()
    host = '0.0.0.0'
    port = 5000
    app.run(debug = True)
