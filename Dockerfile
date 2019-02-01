FROM python:3
MAINTAINER Josh Mandel

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV FLASK_APP /usr/src/app/app.py
ENV UWSGI_PORT 5000
EXPOSE 5000

CMD ["uwsgi", "uwsgi.ini"]
