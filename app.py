from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_resume():
    return send_file('Raahim_Irfan_resume.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    print('Server running at http://localhost:5000')
    print('Your resume is available at http://localhost:5000')
