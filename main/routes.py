from main import app, render_template

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')