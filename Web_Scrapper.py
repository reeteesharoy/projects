#Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import newspaper
import json
import nltk
nltk.download('punkt')
#Ask for user input
url = input("Link of the article:  " )

#GET request to the URL
response = requests.get(url)

#To check if it was successful(status code: 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    article = newspaper.Article(url=url, language='en')
    article.download()
    article.parse() #Downloading and parsing the article
else:  
    print ("Failed to retireve article. Please check the URL and try again")   
    exit()
#Perform natural language processing tasks on the article's content
article.nlp()

#Making a dictionary to store all the output
article_dict = {
    "Title": article.title,
    "Text": article.text,
    "Authors": ', '.join(article.authors) or 'No authors listed.',
    "Published Date": article.publish_date.strftime('%Y-%m-%d %H:%M:%S') or 'No publish date available.',
    "Top Image URL": article.top_image or 'No top image available.',
    "Keywords": ', '.join(article.keywords) or 'No keywords available.',
    "Summary": article.summary or 'No summary available.',
    "Meta Description": article.meta_description or 'No meta description available.',
    "Meta Keywords": article.meta_keywords or 'No meta keywords available.',
    "Meta Language": article.meta_lang or 'No meta language available.',
    "Canonical Link": article.canonical_link or 'No canonical link available.',
    "Source URL": article.source_url or 'No source URL available.',
    "Tags": article.tags or 'No tags available.',
    "Images": article.images or 'No images available.',
    "Videos": article.movies or 'No videos available.'
}
# Iterate through the dictionary and print each key-value pair
for key, value in article_dict.items() :
   print(f"{key} :\n{value}\n\n")