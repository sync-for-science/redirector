from flask import abort, Flask, redirect, request, url_for


app = Flask(__name__)


@app.route('/authorized', methods=['GET', 'POST'])
def authorized():
    if request.method == 'POST':
        # request.values checks query string and posted form data
        code = request.values['code']
        state = request.values['state']
        url = url_for(
            'authorized',
            code=code,
            state=state,
            method='post'
        )
        return redirect(url)
    return 'Redirect successful.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
