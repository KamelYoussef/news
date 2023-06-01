import nltk
nltk.download('punkt')
from newspaper import Article
url = "https://www.zdnet.com/article/what-is-ai-heres-everything-you-need-to-know-about-artificial-intelligence/"
article = Article(url)
article.download()
article.parse()

article.nlp()
print(article.summary)