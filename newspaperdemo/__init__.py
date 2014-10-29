from flask import Flask, request, render_template, redirect, url_for
from newspaper import Article
from xml.etree  import ElementTree

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles/show')
def show_article():
    url_to_clean = request.args.get('url_to_clean')
    if not url_to_clean:
        return redirect(url_for('index'))

    article = Article(url_to_clean)
    article.download()
    article.parse()

    html_string = ElementTree.tostring(article.clean_top_node)

    article.nlp()

    a = {
          'html': html_string, 
         'authors': str(', '.join(article.authors)), 
         'title': article.title,
         'text': article.text,
         'top_image': article.top_image,
         'videos': str(', '.join(article.movies)),
         'keywords': str(', '.join(article.keywords)),
         'summary': article.summary
         }
    return render_template('article/index.html', article=a, url=url_to_clean)
    