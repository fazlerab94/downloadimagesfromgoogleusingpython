#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin


# In[17]:


def download_images(person_name,num_images):
    # Create a directory to store the downloaded images
    if not os.path.exists(person_name):
        os.makedirs(person_name)


# In[19]:


query = quote ("person_name")


# In[21]:


url =f"https://www.google.com/search?q={query}&tbm=isch"


# In[23]:


response = requests.get(url)
response.raise_for_status()


# In[37]:


soup = BeautifulSoup(response.text, "html.parser")


# In[38]:


results = soup.find_all ("img")


# In[40]:


count = 0
image_path = []
for res in results:
    try:
        # Send a GET request to download the image
        link = res['src']
        if not link.startswith("http"):
            link=urljoin(url,link)
        response = requests.get(link)
        response.raise_for_status()
        
        with open(f"{person_name}/{count+1}.jpg","wb") as file:
            file.write(response.content)
        count += 1
    except Exception as e:
            print(f"Error downloading image {count+1}: {str(e)}")
    


# In[41]:


print(f"Downloaded {count} images of {person_name}.")


# In[42]:


person_name = input("Enter the person's name: ")
num_images = 50


# In[43]:


download_images("person_name", "num_images")


# In[ ]:





# In[ ]:




