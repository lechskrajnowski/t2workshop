# Greetings!
# This is a simple Flask app for the Global Azure Workshop 2025.
# It allows users to add comments from the browser.

from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

comments = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        comment = request.form.get('comment')
        if comment:
            comments.append(comment)
        return redirect(url_for('home'))
    return render_template_string('''
        <h1>Hello, Global Azure Workshop 2025!</h1>
        <h2>Greetings!</h2>
        <form method="post">
            <input name="comment" placeholder="Add your comment" required>
            <button type="submit">Add Comment</button>
        </form>
        <h3>Comments:</h3>
        <ul>
        {% for c in comments %}
            <li>{{ c }}</li>
        {% endfor %}
        </ul>
    ''', comments=comments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)