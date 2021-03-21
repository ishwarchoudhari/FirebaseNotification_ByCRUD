from flask import Flask, Response, redirect, url_for, request, session, abort, render_template, flash, message_flashed
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='ac68b1a942de93ceb3141aad')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

users = [User(id) for id in range(1, 21)]

@app.route('/')
@login_required
def home():
    return render_template('login.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        print('Username is ', username)
        password = request.form['password']
        print('Password', password)
        if password == username :
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return render_template('bell.html')
        else:
            flash('No User Name with'+username,'registered Please Register and Login Again')
            return abort(401)
    else:
        return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

@app.errorhandler(401)
def page_not_found(e):
    return render_template('error.html')

@login_manager.user_loader
def load_user(userid):
    return User(userid)

if __name__ == "__main__":
    app.run()