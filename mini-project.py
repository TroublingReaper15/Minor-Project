import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # check for minimum length
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long")
    else:
        score += 1

    # check for uppercase letter
    if not re.search(r'[A-Z]', password):
        suggestions.append("Password should contain at least one uppercase letter")
    else:
        score += 1

    # check for lowercase letter
    if not re.search(r'[a-z]', password):
        suggestions.append("Password should contain at least one lowercase letter")
    else:
        score += 1

    # check for numeric digit
    if not re.search(r'\d', password):
        suggestions.append("Password should contain at least one numeric digit")
    else:
        score += 1

    # check for special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")
    else:
        score += 1

    return score, suggestions

password = input("Input a password: ")
strength = check_password_strength(password)

if strength[0] == 5:
    print("Strong password")
elif strength[0] >= 3:
    print("Moderate password")
else:
    print("Weak password")

if strength[1]:
    print("Suggestions for improvement:")
    for suggestion in strength[1]:
        print("- " + suggestion)