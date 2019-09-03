# Stop words in Kannada

## Creating the corpus

Udayavani is an online Kannada newspaper ([Link](https://www.udayavani.com/)). Scrapy (Python tool) was used to scrap the website for articles in particular categories. The categories scraped were:

- Bollywood news
- Sandalwood news
- Interviews
- State news
- Sports news
- National news
- World news
- Tech news

The articles that had more than 500 words were filtered and the title, content and URL of the article were stored in JSON format. There were a total of 155 articles and were stored in "udayavani.json" file. The "crawler" folder contains the settings required to scrape the website. The "crawler/spiders" folder contains the spider for following the links on the website.

To get the corpus, run the following command

```python  main.py &>  main.out```


## Getting stop words

"udayavani.json" file was read and blobs were created from the ”content” part of the JSON line using textblob module. The words in each blob was read and a dictionary which computes the frequency of each word was stored. The dictionary was sorted in descending order of frequency and the top 102 words were printed (102 words because 2 of the words in the stop list were numbers).

To get the list of stop words, run the following command

```python  stopwords_find.py```


## Stop Words

[List of stop words](./stop-words.txt)

The list of stop words contained a pretty standard set of stop words, i.e.  most of the words were common words that occur in the language. Due to the limited number of articles (155), a couple of numbers appeared in the list as well. A few underlined words which mean Cinema, Day, Kannada, Work, People, Answer and Situation were a bit surprising because they are not stop words. But, because of the fewer articles, it is possible for these words to have crept in.
