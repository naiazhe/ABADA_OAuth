from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

oauth = OAuth(app)

github = oauth.register(
    name='github',
    client_id='Ov23limx1XICnSQ4hvWr',
    client_secret='21af8752f82bf05c8631298422e02cabf775c824',

    access_token_url='https://github.com/login/oauth/access_token',

    authorize_url='https://github.com/login/oauth/authorize',

    api_base_url='https://api.github.com/',

    client_kwargs={
        'scope': 'user:email',
    },
)

# HOME PAGE
@app.route('/')
def home():
    return '<h1>GitHub OAuth Login</h1><a href="/login">Login with GitHub</a>'


# LOGIN ROUTE
@app.route('/login')
def login():
    return github.authorize_redirect(url_for('callback', _external=True))


# CALLBACK ROUTE
@app.route('/callback')
def callback():

    token = github.authorize_access_token()

    user = github.get('user').json()

    session['user'] = user

    return redirect('/profile')


# PROTECTED PROFILE PAGE
@app.route('/profile')
def profile():

    if 'user' not in session:
        return "Unauthorized", 401

    return jsonify(session['user'])


# BONUS PROTECTED API
@app.route('/api/secure-data')
def secure_data():

    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "message": "This is protected secure data.",
        "user": session['user']['login']
    })


# LOGOUT ROUTE
@app.route('/logout')
def logout():

    session.pop('user', None)

    return "Logged out successfully."


if __name__ == '__main__':
    app.run(debug=True)