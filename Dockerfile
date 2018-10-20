FROM python:alpine

ADD ./requirements.txt /opt/webapp/

WORKDIR /opt/webapp

RUN pip install -r requirements.txt

ADD . /opt/webapp

EXPOSE 8080

CMD python /opt/webapp/app.py
