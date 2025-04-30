from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long")
    else:
        score += 1

    if not re.search(r'[A-Z]', password):
        suggestions.append("Password should contain at least one uppercase letter")
    else:
        score += 1

    if not re.search(r'[a-z]', password):
        suggestions.append("Password should contain at least one lowercase letter")
    else:
        score += 1

    if not re.search(r'\d', password):
        suggestions.append("Password should contain at least one numeric digit")
    else:
        score += 1

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")
    else:
        score += 1

    if score == 5:
        status = "Strong"
    elif score >= 3:
        status = "Moderate"
    else:
        status = "Weak"

    return status, suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    status = None
    suggestions = []
    password = ""

    if request.method == 'POST':
        password = request.form['password']
        status, suggestions = check_password_strength(password)

    return render_template('index.html', status=status, suggestions=suggestions, password=password)

if __name__ == '__main__':
    app.run(debug=True)
