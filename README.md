# Redirector

Tiny Flask app which exposes a redirect URI useful for testing OAuth2 workflows. In particular, POST requests to the endpoint will be redirected with any posted form data moved to the query string and an additional parameter added to indicate the POST. The [test suite](https://github.com/sync-for-science/test-suite) can check for this parameter.

## Installation and Operation

    $ pip install -r requirements.txt
    $ uwsgi uwsgi.ini
