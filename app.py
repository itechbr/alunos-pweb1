import os
import frontmatter
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pessoas_dir = os.path.join(os.path.dirname(__file__), 'pessoas')
    pessoas = []
    for pessoa_nome in os.listdir(pessoas_dir):
        readme_path = os.path.join(pessoas_dir, pessoa_nome, 'readme.md')
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                pessoas.append(post.metadata)
    return render_template('index.html', pessoas=pessoas)

if __name__ == '__main__':
    app.run(debug=True)