TravelBlog (Diary of Journey)

A Django travel journal application where users can sign up, log in, create travel posts, and view post details with comments.


TECH STACK
- Django 3.1.6
- SQLite (default local database)
- Bootstrap 5 (UI)
- django-ckeditor 6.3.0 (RichTextField for post description and comment body)


FEATURES
- Public homepage with responsive post cards and pagination
- User authentication (sign up, log in, log out)
- Create / edit / delete posts (login required)
- Public post detail page (shareable URL) with comments
- Admin/superuser pages for managing posts/comments


PROJECT STRUCTURE (high level)
- travelblog/               Django project root (contains manage.py)
- travelblog/travelblog/    Project settings/urls/wsgi
- travelblog/journey/       Main app (models, views, urls, templates)
- requirements.txt          Python dependencies


SETUP (LOCAL)
1) Create and activate a virtual environment
   Windows (PowerShell):
   - python -m venv .venv
   - .\.venv\Scripts\Activate.ps1

2) Install dependencies
   - pip install -r requirements.txt

3) Run migrations
   From the travelblog folder:
   - python manage.py makemigrations
   - python manage.py migrate

4) Create a superuser (optional, for admin)
   - python manage.py createsuperuser

5) Run the server
   - python manage.py runserver

Open the site:
- Home: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/accounts/login/
- Signup: http://127.0.0.1:8000/signup
- Admin: http://127.0.0.1:8000/admin/


IMPORTANT URLS (journey app)
- / or /post_list
  Homepage post list (paginated)

- /post/create/
  Create a post (login required)

- /post/<pk>/edit/
  Edit a post (login required)

- /post/<pk>/delete/
  Delete a post (login required)

- /travelblog_post/<post_id>
  Post detail page (shareable/public). Shows post + comments.

- /comment_list
  Comment list (login required)

- /post_detail
  Admin-style posts list (login required)


DATABASE
- Local default database is SQLite at:
  travelblog/db.sqlite3


NOTES ABOUT CKEDITOR (RichTextField)
- The project uses CKEditor for rich text editing.
- The editor height is configured in travelblog/settings.py via CKEDITOR_CONFIGS.


DEPLOYMENT NOTES (PYTHONANYWHERE)
General steps (high level):
1) Upload/clone the repo on PythonAnywhere.
2) Create a virtualenv and install requirements:
   - pip install -r requirements.txt
3) Run migrations:
   - python manage.py migrate
4) Collect static files (important for CKEditor assets):
   - python manage.py collectstatic
5) Configure the PythonAnywhere Web App WSGI file to point to your project.


TROUBLESHOOTING
- If a name is not showing for a user/superuser:
  Some accounts may have blank first/last name. Templates use a username fallback.

- If CKEditor assets are missing in production:
  Run collectstatic and verify STATIC_ROOT/STATIC_URL settings.
