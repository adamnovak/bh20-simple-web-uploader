# Simple Web Uploader for Public SARS-CoV-2 Sequence Resource

This project is a simple web server that lets you use [the Sequence Uploader](https://github.com/arvados/bh20-seq-resource#sequence-uploader) from a browser.

To run it locally:

```
virtualenv --python python3 venv
. venv/bin/activate
pip install -e .
env FLASK_APP=bh20simplewebuploader/main.py flask run
```

Then visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Production

For production deployment, you can use [gunicorn](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/#gunicorn):

```
pip3 install gunicorn
gunicorn bh20simplewebuploader.main:app
```

This runs on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default, but can be adjusted with various [gunicorn options](http://docs.gunicorn.org/en/latest/run.html#commonly-used-arguments)

## GNU Guix

To run the web uploader in a GNU Guix container

```
guix environment -C guix --ad-hoc git python python-flask python-pyyaml nss-certs --network openssl
```

and

```
env FLASK_APP=bh20simplewebuploader/main.py flask run
```
