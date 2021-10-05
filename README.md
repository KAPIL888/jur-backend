# Jur

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KAPIL888/jur-backend.git
$ cd jur-backend/demoBackend
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv  env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

If migrations are not working delete migration folder and run:
```sh
(env)$cd jur-backend/demoBackend
(env)$cd python manage.py makemigrations demoBackend
(env)$cd python manage.py migrate
```



Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
use this to `http://127.0.0.1:8000/`.
