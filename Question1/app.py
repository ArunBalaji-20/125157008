from flask import Flask,render_template,render_template_string

app=Flask(__name__)

@app.route('/')
def home():
    return render_template_string('hi')

if __name__=='__main__':
    app.run()