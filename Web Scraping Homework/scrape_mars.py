#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as BS
import requests
import shutil
from IPython.display import Image
import pandas as pd

def scrape_all():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    #scrape the page into the soup
    html = browser.html
    soup = BS(html, "html.parser")

    #Print sample of one article 
    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    print(f"Title: {news_title}")
    print(f"Para: {news_paragraph}")

    #Visit Image URL
    url2 = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)

    #Scrape the page again
    html = browser.html
    soup = BS(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    img_url = "https://jpl.nasa.gov"+image
    featured_image_url = img_url
    response = requests.get(img_url, stream=True)
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    # Display the image with IPython.display
    Image(url='img.jpg')


    #open twitter weather browwer
    mars_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather)

    #scrape the page into soup
    html = browser.html
    soup = BS(html, "html.parser")

    #print tweet text
    mars_tweet = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(f"Tweet: {mars_tweet}")

    #scraping facts using Pandas


    url = 'https://space-facts.com/mars/'

    mars_tables = pd.read_html(url , encoding= "utf-8")
    mars_tables

    df = mars_tables[0]
    df.columns = ['Attributes', 'Value']
    df.head()

    #Scrape the moon name and image and put into a dictionary
    hemisphere_images_list = []
    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url4)
    #click on the first moon
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    #Scrape the text
    html = browser.html
    soup = BS(html, "html.parser")
    picture_url = soup.find("img", class_="thumb")["src"]
    # create a dictionary 
    link_dict = {"title": "Cerberus Hemisphere Enhanced", "img_url": picture_url}
    hemisphere_images_list.append(link_dict)

    # go back to previous page
    browser.back()
    # Click on the second moon
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    # Load the html, parse for the image
    html = browser.html
    soup = BS(html, 'html.parser')
    picture_url = soup.find("img", class_="thumb")["src"]
    # create containers from the scraped information
    
    link_dict = {"title": "Schiaparelli Hemisphere Enhanced", "img_url": picture_url}
    hemisphere_images_list.append(link_dict)


    # go back to previous page
    browser.back()

    # Click on the hemisphere link to open the html of the high quality image
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    # Load the html, parse for the image, and store the image in the "link" variable
    html = browser.html
    soup = BS(html, 'html.parser')
    picture_url = soup.find("img", class_="thumb")["src"]
    
    # create containers from the scraped information
    link_dict = {"title": "Syrtis Major Hemisphere", "img_url": picture_url}
    hemisphere_images_list.append(link_dict)


    #go back to previous page
    browser.back()

    # Click on the hemisphere link to open the html of the high quality image
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    # Load the html, parse for the image, and store the image in the "link" variable
    html = browser.html
    soup = BS(html, 'html.parser')
    picture_url = soup.find("img", class_="thumb")["src"]
    
    # create containers from the scraped information
    link_dict = {"title": "Valles Marineris Hemisphere", "img_url": picture_url}
    hemisphere_images_list.append(link_dict)
    # close the browser
    browser.quit()

    #store scrapped data into a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "image": image,
        "mars_tweet": mars_tweet,
        "picture_url": picture_url,



    }

    return mars_data




# In[ ]:




