from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY']='super-secret-key'

username = "Guy"
password = "123"
facebook_friends=["Itay","Ido","Eyal", "Yair", "Shachar", "Noy", "Jihad"]

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if request.form['username'] == username and request.form['password'] == password:
			return redirect(url_for('homepage'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/home')
def homepage():
	return render_template('home.html',
	 facebook_friends=facebook_friends
)

@app.route('/friends_exists/<string:friend>')
def friendsExists(friend):
	if friend in facebook_friends:
		return render_template('friend_exists.html', f = True)
	else:
		return render_template('friend_exists.html', f = False)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)