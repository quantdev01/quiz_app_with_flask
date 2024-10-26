from main import app, render_template

@app.route('/home')
def home_page():
    return render_template('home.html')