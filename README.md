# OAuth Flask GitHub Login Project

## Features
- GitHub OAuth Login
- Protected Routes (/profile)
- Session Authentication
- Logout Functionality
- Secure API Endpoint

## How to Run

1. Install dependencies:
   python -m pip install -r requirements.txt

2. Run the app:
   python app.py

3. Open browser:
   http://localhost:5000/login


## Result Analysis Answers

**Activity for BIT321 SYSTEM INTEGRATION [LAB]**


i. What happens when a user accesses /profile without logging in?

The application checks for an active user session. If none is found, it will denies access and returns an “Unauthorized” message with HTTP status code 401, indicating that login is really required.

ii. What data is returned after successful login?

After successful login the application show my github information such as username, link to my profile ID, name, avatar, email, profile URL, and other infomation that are related to my github account.

iii. Why is OAuth more secure?

OAuth is more secure because the application does not store or handle the user passwords directly. Authentication is handled by trusted providers like GitHub.

iv. What challenges did you encounter?

The possible challenges include incorrect callback URLs, which I personally experienced during the setup. The issue happened because the callback URL in the GitHub OAuth settings did not exactly match the URL used in the Flask application (I use the 127.0.1 instead of 127.0.0.1). Since GitHub requires an exact match, the process failed until the correct URL was matched. Other challenges include invalid client credentials, where incorrect Client ID or Client Secret can prevent authentication from working, and dependency installation issues such as missing or unrecognized pip commands during setup.

v. What did you learn?

Through this activity, I learned how OAuth works and how to implement GitHub login using Flask. I also learned how to secure routes using session-based authentication to protect endpoints from unauthorized access. The OAuth allows users to log in using third-party accounts without sharing passwords directly with the application, making it convenience for users and reduces the risk of password-related vulnerabilities.
