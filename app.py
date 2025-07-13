from flask import Flask, jsonify
app = Flask(__name__)
# Route: base URL
@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask CI/CD!'})
# Route: health check
@app.route('/health')
def health():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(debug=True)