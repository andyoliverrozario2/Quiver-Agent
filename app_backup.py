from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User  # Import the User model from models.py

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random key

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # This tells Flask-Login which route to redirect if not logged in

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # For now, we're just hardcoding a single user.
    # In a real application, you'd look up the user in your database.
    if user_id == "1":
        return User(1, "test", "password")
    return None

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # For our MVP, we check for a hardcoded test user
        if username == 'test' and password == 'password':
            user = User(1, username, password)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template('login.html')

# Protected route for the dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return f"Welcome to QuiverAgent Dashboard, {current_user.username}!"

# Route for logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
