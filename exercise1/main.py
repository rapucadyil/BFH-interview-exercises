# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/multiply')
def multiply():
    integer1 = request.args.get('integer1')
    integer2 = request.args.get('integer2')

    return '''<h1>The value of {} * {} is : {}</h1>'''.format(integer1, integer2, int(integer1) * int(integer2))

@app.route('/integer-example')
def integer_example():
   # if key doesn't exist, returns None
    integer = request.args.get('integer1')

    return '''<h1>The integer value is: {}</h1>'''.format(integer)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(port=105)