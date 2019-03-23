from flask import Flask,request,jsonify
import requests
app=Flask(__name__)


@app.route('/', methods=['GET'])
def respond():
    name = request.args.get('name')
    print (name)
    res={'name':'Pranav'}
    return jsonify(res)
      

@app.route('/webhook', methods=['POST'])
def query():
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')
    if intent == 'Default Welcome Intent':
        qtext=req.get('queryResult').get('queryText')
        res={'fulfillmentText':' Recieved ' + qtext}
        return jsonify(res)
    elif intent == 'number':
        qtype= req.get('queryResult').get('parameters').get('type')[0]
        num = req.get ('queryResult').get('parameters').get('number') 
        num = int(num)
        print(num, type(num))
        url = 'http://numbersapi.com/'
        final_url = url + str(num) + '/' + qtype + '?json'
        res = requests.get(final_url) 
        print(res)
        text = res.json()['text']

    return jsonify({'fulfillmentText': text})
  
    return jsonify({'fulfillmentText':'error'})



if __name__=="__main__":
    app.run()
