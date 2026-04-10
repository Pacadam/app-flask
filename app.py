from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Bonjour depuis Flask !</h1><p>Le pipeline CI/CD fonctionne. 🚀</p>'


@app.route('/sante')
def sante():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
