from logging import debug
from flask import Flask #importing the Flask class object from the flask library

app=Flask(__name__) # instantiate the class object, __name__ is the 

# decorator
@app.route('/')
def home():
    return "Space Exploration!"

# decorator
@app.route('/us/')
def us():
    return "Mercury, Gemini, Apollo, Space Shuttle, Crew Dragon, New Shepard, Spaceshiptwo"

@app.route('/russia/')
def russia():
    x = "Vostok, Voskhod, Soyuz"
    return x

@app.route('/china/')
def china():
    return "Shenzhou"

# when a python file is being executed, it will assign __main__ to __name__
if __name__== "__main__":
    app.run(debug=True)