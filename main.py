# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, jsonify
from flask import render_template
import Data


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

app = Flask(__name__)

list = {"Question": """Un observador O’sostiene una regla de 1 m la cual forma un angulo de 30◦ con la direccion
positiva del eje x’. O’viaja en la direcci ́on positiva del eje x (co-lineal con x’) con velocidad de 0,8c 
respecto al observador O. ¿Cuales son la longitud de la regla medidos por O?""","Answer": "0.72 m"}

@app.route("/json")
def json():
	return jsonify(list)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/instagram")
def instagram():
    count_comment = len(Data.tweets[0].comment)
    count_likes = len(Data.tweets[0].likes)
    return render_template("instagram.html", CountShare="12 mil", CountComment=count_comment,
                           CountLikes=count_likes, tweets=Data.tweets)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}'


# url_for('hello', filename='style.css')


if __name__ == '__main__':
    app.debug = True;
    app.run(host="0.0.0.0");
    app.run();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
