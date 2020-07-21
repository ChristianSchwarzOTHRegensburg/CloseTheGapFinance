from GoogleNews import GoogleNews
from wordcloud import WordCloud
#for wordcloud to work you need to install microsoft c++ Build Tools --> VS Download Page
import matplotlib.pyplot as plt

googlenews = GoogleNews("en", "m" )
#Parameters: language and timeframe (day, month, year)

googlenews.search("WTI Price")

googlenews.getpage(1)
#first Result Page

headlines = googlenews.gettext()
#only show Headlines (pictures or links are also available)

text = ' '.join([str(elem) for elem in headlines])
#convert to string, Because Wordcloud expects string like object


#Generate the Wordcloud
wordcloud = WordCloud(max_font_size=50).generate(text) 
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

googlenews.clear()
