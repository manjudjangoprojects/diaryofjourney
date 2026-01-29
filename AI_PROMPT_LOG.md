# Project Prompt Log

## 2026-01-26


### 1

- **Prompt**
  - Failed to build psycopg2
  - ERROR: Could not build wheels for psycopg2, which is required to install pyproject.toml-based projects - how to fix this
- **Answer**
  - Explained this happens when `pip` can’t use a prebuilt wheel and tries to compile.
  - Recommended using `psycopg2-binary` (fastest) or switching to `psycopg` v3.
  - Provided source-build steps (MSVC + PostgreSQL headers) if you must compile.

### 2

- **Prompt**
  - python version 3.11.9
- **Answer**
  - Explained Python 3.11 often triggers source builds when a wheel isn’t available.
  - Recommended `psycopg2-binary` or `psycopg[binary]`.
  - Listed source-build requirements if you must use `psycopg2`.

### 3

- **Prompt**
  - I am using django and I will be hosting in pythonanywhere website
- **Answer**
  - Recommended platform-specific dependencies so Windows uses `psycopg2-binary` and Linux (PythonAnywhere) can use `psycopg2`.
  - Mentioned `psycopg2` may not be needed at all unless you’re using PostgreSQL.

### 4

- **Prompt**
  - Record the prompts I am asking for this project and once the project done give me it in a file.
- **Answer**
  - Created `PROMPT_LOG.md` in the project root and started logging your prompts.

### 5

- **Prompt**
  - I am not able to retrieve the image and author name in the server. Please check the error
- **Answer**
  - Checked `models.py`, `views.py`, and `post_list.html`.
  - Fixed missing `timezone` import in `views.py`.
  - Fixed broken HTML quotes in the image link and added fallbacks for missing `image_url` and missing author full name.

### 6

- **Prompt**
  - Have to split the image size in http://127.0.0.1:8000/travelblog_post/1 with visited places, date, favorite place, address and favorite activity. have to split both in equal-height.
- **Answer**
  - Updated `travelblog_post.html` layout to use equal-height split columns and crop the image to fit using `object-fit: cover`.

### 7

- **Prompt**
  - give me a perfect django-ckeditor version to use in Django 3.1.6 and pythonanywhere
- **Answer**
  - Recommended pinning `django-ckeditor==6.3.0` (last release before 6.4.0 dropped Django<3.2).
  - Noted to run `collectstatic` on PythonAnywhere and keep Django pinned to 3.1.6.

### 8

- **Prompt**
  - I am not able to retrieve the image and author name in the server. Please check the error
- **Answer**
  - Checked `models.py`, `views.py`, and `post_list.html`.
  - Fixed missing `timezone` import in `views.py`.
  - Fixed broken HTML quotes in the image link and added fallbacks for missing `image_url` and missing author full name.


### 9

- **Prompt**
  - Need to improve the sign up and login page visually. Help me with adding better bootstrap
- **Answer**
  - Updated `signup.html` and `registration/login.html` to use Bootstrap card layouts, better spacing, and primary/secondary buttons.
  - Added a small script to apply Bootstrap `form-control` classes to form fields rendered by `as_p`.

### 10

- **Prompt**
  - Homepage - Make it more attractive by adding more styles using bootstrap and make sure it should be responsive in mobile, tablet and desktop
- **Answer**
  - Redesigned the homepage post grid using Bootstrap cards, responsive `row-cols-*` layout, and a hero-style header.
  - Updated pagination to Bootstrap pagination UI so it looks good on mobile and desktop.

### 11

- **Prompt**
  - Title Bar is not attractive. Make it visually appeal and I feel like it has more gaps.
- **Answer**
  - Restyled the navbar into a dark Bootstrap app bar (less padding, better alignment) and reduced header vertical padding to remove excessive gaps.

### 12

- **Prompt**
  - http://127.0.0.1:8000/post/create/ change this edit post to visually pleasing
- **Answer**
  - Updated `post_new.html` and `post_edit.html` with Bootstrap card layouts, better spacing, and styled buttons.
  - Added a small script to apply Bootstrap `form-control` classes to fields rendered via `as_p`.

### 13

- **Prompt**
  - Description is RichTextField so it is looking bigger could you please check and adjust the size accordingly
- **Answer**
  - Reduced the CKEditor (RichTextField) editor height on `post_new.html` and `post_edit.html` using CSS targeting `.django-ckeditor-widget .cke_contents`.

### 14

- **Prompt**
  - Nope it doesn't work
- **Answer**
  - Added `CKEDITOR_CONFIGS` in `settings.py` to set a reliable global CKEditor height (`height: 220`) so RichTextField editors render smaller.

### 15

- **Prompt**
  - superuser name is not visible after logging into the application. I created test user it is visible after log in
- **Answer**
  - Fixed navbar display to fall back to `user.username` when `user.get_full_name` is blank using `{% firstof user.get_full_name user.username %}`.

### 16

- **Prompt**
  - travelblog_post.html retrieving user name but not superuser name
- **Answer**
  - Updated `travelblog_post.html` to fall back to `post.author.username` when `post.author.get_full_name` is blank.

### 17

- **Prompt**
  - `<h2>{% firstof post.author.get_full_name post.author.username %}</h2> - change this in italics`
- **Answer**
  - Added Bootstrap `fst-italic` class to render the author name in italics.

### 18

- **Prompt**
  - I don't want to display the visited date in the home page card body instead display the uploaded date in the homepage card body
- **Answer**
  - Updated `post_list.html` to display `post.created` (uploaded date) instead of `post.visited_date`.

### 19

- **Prompt**
  - Could you please add readme.txt file for this project for user to understand this from GitHub
- **Answer**
  - Created `readme.txt` in the project root with project overview, features, local setup steps, important URLs, database notes, CKEditor notes, and deployment tips.



