# Python-Django-Banao-Task-1
Signup and login for different types of users
Project Title: user_portal
This is a Django-based web application that allows two types of users — Patients and Doctors — to sign up, log in, and access separate dashboards based on their roles. It demonstrates the implementation of a custom user model, form validation, user authentication, and media upload handling (profile pictures).
Key Features:
•	Custom User Model (CustomUser with user_type: Doctor or Patient)
•	Signup form with:
o	First name, Last name
o	Profile picture
o	Username, Email
o	Password + Confirm Password validation
o	Address (line 1, city, state, pincode)
•	 Login system using Django’s built-in authentication
•	 Role-based dashboard redirect after login:
o	Doctors go to /doctor_dashboard/
o	Patients go to /patient_dashboard/
•	Dashboard displays user details from signup
•	Profile Picture upload and display
•	Password confirmation check during signup
•	Basic Bootstrap-based responsive UI (optional add-on)
Technologies Used:
•	Python 3.x
•	Django 4.x+
•	SQLite (default DB)
•	HTML/CSS (Bootstrap Optional)
•	Pillow (for image upload handling)
 Setup Instructions (for local run)
Clone the repo and navigate into it:
bash
git clone https://github.com/yourusername/user_portal.git
cd user_portal
Create and activate a virtual environment:
python -m virtualenv env
env\Scripts\activate        # On Windows
Install dependencies:
bash
o	pip install asgiref==3.8.1
o	Django==5.2.3
o	pillow==11.2.1
o	sqlparse==0.5.3
o	typing_extensions==4.14.0
o	tzdata==2025.2
Run migrations:
bash
python manage.py makemigrations
python manage.py migrate
Run the server:
bash
python manage.py runserver
Open your browser at http://127.0.0.1:8000/signup/ to register.

