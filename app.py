from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# メモリ内に投稿を保持するリスト
posts = []

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        if content:
            posts.append(content)
        return redirect(url_for('index'))
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)


