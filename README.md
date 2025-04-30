Minor Project - Password Strength Checker
This is a Password Strength Checker web application built using Flask as the backend, along with HTML, CSS, and Python for the frontend and logic. The project checks the strength of a given password based on multiple criteria and provides feedback and suggestions for improvement.

Project Features
1. Password Strength Evaluation: The app evaluates the strength of the password based on length, character variety (uppercase, lowercase, numeric, special characters), and gives a score.
2. Suggestions: If the password is weak or moderate, the app suggests improvements to make it stronger.
3. User-Friendly Interface: The interface is simple and interactive, providing a responsive and modern design with intuitive feedback.

Technologies Used
  Backend: Flask (Python)
  Frontend: HTML, CSS
  Logic: Python for evaluating password strength
  Libraries:
    Flask for backend server
    re (regular expressions) for evaluating password characteristics

Setup Instructions
Follow these steps to set up and run the project locally:

Prerequisites
  1. Install Python 3 (version 3.x).
  2. Install pip (Python package manager).
   
Installation Steps
1. Clone the repository to your local machine:
     git clone https://github.com/TroublingReaper15/Minor-Project.git
     cd Minor-Project
2. Create a virtual environment (optional but recommended):
     python3 -m venv venv
     source venv/bin/activate  # For Linux/macOS
     venv\Scripts\activate  # For Windows
3. Install the required Python packages:
     pip install -r requirements.txt
4. Run the Flask application:
     python app.py
5. Open a web browser and navigate to:
     http://127.0.0.1:5000/
   
You should now be able to see the Password Strength Checker in action!

Minor-Project/
├── app.py              # Main Python file (Flask backend)
├── requirements.txt    # List of required Python packages
├── templates/          # HTML templates for rendering the frontend
│   └── index.html      # The main template for password checker form and results
└── static/             # Static files for CSS and other assets
    └── style.css       # Custom styles for the web page

Testing the Password Strength
1. Enter any password in the input field.
2. Click the "Check Strength" button.
3. The app will analyze the password and display the strength (Weak, Moderate, or Strong) along with suggestions to improve the password.

Example
  Strong Password: StrongPassword123!
  Moderate Password: Password123
  Weak Password: 12345

Customizing the Application
You can modify the following:
1. The password criteria in check_password_strength() function inside app.py.
2. The frontend design (HTML/CSS) as per your requirements.
3. Add any additional features like password complexity scoring, user registration/login system, etc.

 
