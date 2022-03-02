from flask import Flask, render_template, request, jsonify
from chatBot import chatBot
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quetion = request.form
        queryl = list(quetion.keys())
        query = queryl[0]
        response = chatBot.chatbot_response(query)
        print(response)
        response = {"Message": response}
        return response
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='192.168.8.103')
