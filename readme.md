# DJANGO ECOMMERCE PBL6

![](https://img.shields.io/badge/Django-3.1.2-green)
![](https://img.shields.io/badge/Python-3.4-green)

Các package yêu cầu:
-------------
Tất cả các package: [requirements.txt](https://github.com/nhantruong2712/ecommerce-django-pbl6/blob/master/requirements.txt)

Hướng dẫn cài đặt (Windows)
-------------
Yêu cầu phiên bản python và django
+ Python 3.4
+ Django 3.1.2

Cài đặt môi trường ảo (virtual environment):
```
$ pip install virtualenv
$ virtualenv venv
```
Kích hoạt môi trường ảo:
```
$ venv/Scripts/activate
```
Cài đặt các package và cập nhật database bằng các câu lệnh sau:
```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```
Sau đó tạo tài khoản admin và chạy server
```
$ python manage.py createsuperuser
$ python manage.py runserver
```
Đăng ký tài khoản và tên miền tại website https://pagekite.net
Tiến hành tải pagekite về: 
```
curl -o https://pagekite.net/pk/pagekite.py 
```
Run server pagekite
```
cd to your project
$ python pagekite.py 80 your_pagekite_domain
```
Hướng dẫn cài đặt (Linux)
-------------

Cài đặt môi trường ảo (virtual environment):
```
$ pip install virtualenv
$ virtualenv venv
```
Kích hoạt môi trường ảo:
```
$ source venv/bin/activate
```
Cài đặt các package và cập nhật database bằng các câu lệnh sau:
```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```
Sau đó tạo tài khoản admin và chạy server
```
$ python manage.py createsuperuser
$ python manage.py runserver
```
Tiến hành tải pagekite về và cài đặt nginx, gunicorn:
```
$ pip install django gunicorn psycopg2
$ sudo apt install pagekite
$ sudo nano /etc/systemd/system/gunicorn.service
```
Config gunicorn (thay your user thành user ubuntu của bạn và đường dẫn tương ứng)
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=your_user
Group=www-data
WorkingDirectory=/home/your_user/myproject
ExecStart=/home/your_user/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/your_user/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```
```
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
```
Check status gunicorn 
```
$ sudo systemctl status gunicorn
```
Restart gunicorn
```
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn
```
Config nginx
```
$ sudo nano /etc/nginx/sites-available/myproject
```
```
server {
    listen [::]80;
    listen 80;
    server_name your_pagekite_domain;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/your_user/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}
```
Restart nginx and open up firewall
```
$ sudo systemctl restart nginx
$ sudo ufw delete allow 8000
$ sudo ufw allow 'Nginx Full'
```
Run server pagekite
```
cd to your project
$ python pagekite.py 80 your_pagekite_domain
```

