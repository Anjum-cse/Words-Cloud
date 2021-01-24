import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np

currdir = os.path.dirname(__file__)

def get_wiki(query):
    tittle = wikipedia.search(query)[0]
    page =wikipedia.page(tittle)
    return page.content

def create_wordcloud(text):
    mask= np.array(Image.open(os.path.join(currdir,"leaf.png")))
    stopwords =set(STOPWORDS)

    wc= WordCloud(background_color= 'white',
                  mask=mask,
                  stopwords= stopwords,
                  max_words=200
                  )
    wc.generate(text)
    wc.to_file(os.path.join(currdir,"cr7.png"))
create_wordcloud(get_wiki("cristiano ronaldo"))