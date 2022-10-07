import flask


class User():
    id = 0

    def __init__(self, name):
        self.name = name
        self.id = User.id
        User.id += 1


a = User('a')# this is for what?
print(a.id)
b = User('b')
print(b.id)
app1 = flask.Flask(__name__)


@app1.route('/')
def index():
    return flask.render_template('index.html')


@app1.route('/home')
def homepage():
    return flask.render_template('homepage.html')


@app1.route('/things')
@app1.route('/about')
def aboutpage():
    return flask.render_template('about.html')


@app1.route('/user/<string:name>/<int:id>')
def userpage(name, id):
    return f"Hi, {name}, this is your page!\nYour id is: {id}"


@app1.route('/NaslediePredkov')
def Nasledilka():
    return flask.render_template('NaslediePredkov.html')


if __name__ == '__main__':
    app1.run(debug=True)
