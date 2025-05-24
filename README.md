# Learning Log

A Django-based web application that helps users keep track of their learning journey. Users can create topics of interest and make detailed entries about what they've learned.

## Features

- 👤 User Authentication
  - Register new accounts
  - Login/Logout functionality
  - Personal learning logs for each user

- 📚 Topic Management
  - Create new topics
  - View all topics
  - Topics are private to each user

- ✍️ Entry System
  - Add new entries to topics
  - Edit existing entries
  - Entries are timestamped
  - Rich text support with line breaks

- 🎨 Modern UI
  - Bootstrap 5 integration
  - Responsive design
  - Clean and intuitive interface

## Technology Stack

- Python
- Django
- Bootstrap 5
- SQLite3
- HTML/CSS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/learning_log.git
cd learning_log
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install django django-bootstrap5
```

4. Apply the database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin) account:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit `http://localhost:8000` in your web browser to start using the application.

## Usage

1. Register a new account or login with existing credentials
2. Create topics you want to learn about
3. Add entries to your topics to record what you've learned
4. Edit entries as needed to update your learning progress

## Project Structure

- `learning_logs/` - Main application directory
  - `models.py` - Contains Topic and Entry models
  - `views.py` - Application views and logic
  - `urls.py` - URL routing
  - `templates/` - HTML templates
- `users/` - User authentication app
  - `views.py` - User-related views
  - `urls.py` - Authentication URLs
  - `templates/` - User-related templates

## Security Features

- User authentication required for accessing topics and entries
- Each user can only view and edit their own topics and entries
- CSRF protection enabled
- Secure password hashing
- Django's built-in security features

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Documentation
- Bootstrap 5 Documentation
- Python Community 