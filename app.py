from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'This is a simple API endpoint.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
        