import streamlit as st
import urllib.request
from bs4 import BeautifulSoup as bs
import html2text as ht

def url2md(medium_url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    headers={'User-Agent':user_agent,} 
    url="http://webcache.googleusercontent.com/search?q=cache:" + medium_url + "&sca_esv=571285583&strip=1&vwsrc=0"
    
    
    
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
        
    data = response.read()

    divs = bs(data).find_all("div", attrs={"class" : "ch bg fw fx fy fz"})

    for d in divs:
        if 'storyTitle' in str(d): 
            print(d)
            storyTitle = d.find("h1", attrs={"data-testid" : "storyTitle"}).get_text()
            print(storyTitle)
            p1 = d.find("p", attrs={"class" : ["pw-post-body-paragraph"]})
            storyBody = [p1] + p1.find_next_siblings()
            print(p1)

    return storyTitle , storyBody, url

with st.sidebar:
    st.title("[Medium rere]")
    '''**Displays a convenient copy of the page from Google Cache**'''
    medium_url = st.text_input("Write medium url",
                               value="https://medium.com/@trumandaniels/creating-a-machine-learning-application-with-streamlit-ecce038eec5a")
    "Link to a copy of the page in google cache:"

if medium_url:
    storyTitle , storyBody, gcache_url = url2md(medium_url)

    sBody = ">>>>"
    for sb in storyBody: 
        sBody = sBody + str(sb)
        

    st.title(storyTitle)
    st.write(ht.html2text(sBody))

    st.sidebar.write(gcache_url)

