# django-meara
Demo REST API project in Python Django. MEARA stands for Matt's Enterprise Architecture Reports &amp; Analytics.

## Setup (ROUGH DRAFT)
Currently a log of the steps I've taken while starting the project from scratch. I'll have to weed-out the creation steps (e.g. startproject, startapp)

1. Tap the "Multipass" Cask
  ```
  brew cask install multipass
  ```  
2. Spin up a new Ubuntu VM
  ```
  multipass launch --name my-django-demo
  ```
3. Create a local dir to turn into a share point
  ```
  mkdir -p ~/mnt/django-meara
  ```
4. Mount it to the new Ubuntu VM
  ```
  multipass mount ~/mnt/django-meara my-instance:/mnt/django-meara
  ```
5. Log into the new Ubuntu VM
  ```
  multipass shell django-demo
  ```
6. Set up Ubuntu VM
  1. Install Python3 & PIP3
    ```
    sudo apt update
    sudo apt install python3-pip python3-dev
    ```
  2. Symlink pip3 then upgrade it
    ```
    ln -s /usr/bin/pip3 /usr/bin/pip
    pip install --upgrade pip
    ```
  3. Install Django & tools
    ```
    python3 -m pip install django virtualenv gunicorn
    ```
  4. Install and Config PostgreSQL  
    1. APT Install base
      ```
      sudo apt-get install postgresql postgresql-contrib libpq-dev
      ```
    2. Install Python Adapter w PIP
      ```
      pip install psycopg2
      ```
    3. Switch to postgres user and open a shell
      ```
      sudo -u postgres psql
      ```
    4. Set postgres password to 'admin'
      ```
      \password postgres
      Enter new password:
      admin
      ```
    5. Create a new DB & Role for Django
      ```
      CREATE USER python_dev WITH PASSWORD 'aqwe123';
      CREATE DATABASE django_db OWNER python_dev;
      ```
    6. Check
      ```
      \list
      ```
  5. Setup Django Project & Link PSQL
    1. Mount project share point
      ```
      multipass mount ~/mnt/myproject django-srv:/mnt/myproje  
      ```
    2. Create a new virtualenv (from /mnt)
      ```
      python3 -m virtualenv --python=python3 myproject/
      ```
    3. Activate virtualenv
      ```
      cd myproject/
      source bin/activate
      ```
    4. Install Django, gunicorn, & psycopg2 to virtualenv
      ```
      pip install django gunicorn psycopg2
      ```
    5. Start Django project
      ```
      django-admin startproject meara_project
      ```
    6. Update DB & Static folder in settings.py  
      ```
      cd hello_django/
      vim hello_django/settings.py
      ```
      1. To ALLOWED_HOSTS, add the Ubuntu VMs IP address (multipass info my-django-demo)
      2. Use these db settings on line 76
        ```
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'django_db',
                'USER': 'python_dev',
                'PASSWORD': 'aqwe123',
                'HOST': 'localhost',
                'PORT': '',
        ```
      3. Add setting for static root dir at end
        ```
        STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
        ```
      4. Save & exit
    7. Init Django project with credentials, ubuntu:aqwe1234
      ```
      python manage.py migrate
      python manage.py createsuperuser
      python manage.py collectstatic
      ```
    8. You can develop by running the built-in django server
      ```
      pythgon manage.py runserver 0.0.0.0:8080
      ```
    9. Surf to `/admin` folder in a browser e.g. http://192.168.64.3:8080/admin

  6. Configure Gunicorn WSGI
    * TK
  7. Install and Config Supervisor
    * TK
  8. Install and Config Nginx
    * TK
  9. TEST
    * TK
