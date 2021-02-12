from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to home"


@app.route("/bio")
def bio():
    return "This is Jay Bhanushali"


# the rule parameter of route was static in basic app, now it will be dynamic , variable rule - my_name, converter -
# default i.e string
@app.route("/<my_name>")
def greeting(my_name):
    return "Welcome " + my_name + "!"


#variable rule - number, converter : int
@app.route('/square/<int:number>')
def show_square(number):
    return "Square of " + str(number) + " is: " + str(number*number)


if __name__ == "__main__":
    app.run(debug=True)
