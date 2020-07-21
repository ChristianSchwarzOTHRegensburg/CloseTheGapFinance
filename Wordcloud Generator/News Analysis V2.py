from GoogleNews import GoogleNews
from wordcloud import WordCloud
#for wordcloud to work you need to install microsoft c++ Build Tools --> VS Download Page
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root= tk.Tk()
root.title("Wordcloud Generator")

canvas1 = tk.Canvas(root, width = 800, height = 600)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(400,50, window=entry1)

def InputButton():
    x1 = entry1.get()
    label1 = tk.Label(root)
    canvas1.create_window(200, 230, window=label1)
    getNews(x1)
    
button1 = tk.Button(text='Generate Wordcloud', command=InputButton)
canvas1.create_window(400, 80, window=button1)


    
def getNews(text):
    googlenews = GoogleNews("en", "m" )
    #Parameters: language and timeframe (day, month, year)
    googlenews.search(text)
    googlenews.getpage(1)
    #first Result Page
    headlines = googlenews.gettext()
    #only show Headlines (pictures or links are also available)

    #convert to string, Because Wordcloud expects string like object
    text = ' '.join([str(elem) for elem in headlines])
    generateWordCloud(text)
    googlenews.clear()
    return

def generateWordCloud(text):
    wordcloud = WordCloud(max_font_size=50).generate(text) 
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

 
