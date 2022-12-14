from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("start.html")

@app.route('/procForm', methods=['POST'])
def processPost():
    msg1 = request.form['msg1']
    msg2 = request.form['msg2']
    num1 = int(msg1)
    num2 = int(msg2)
    msg=num1 + num2
    return render_template("result.html", message1 = msg1 , message2 = msg2 ,message = msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
