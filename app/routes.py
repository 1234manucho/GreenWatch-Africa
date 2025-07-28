from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
@main.route('/about')
def about():
    return render_template('about.html')
@main.route('/contact')
def contact():  
    return render_template('contact.html')
@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@main.route('/login')
def login():
    return render_template('login.html')
@main.route('/register')
def register():
    return render_template('register.html')