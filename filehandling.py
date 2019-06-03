import re
import os
from urllib.request import urlopen
from simple_colors import *
from urllib.error import HTTPError


# Create one folder for all the scraped pages on the website
def create_project_dir(directory):
    if not os.path.exists(directory):
        print(yellow('Creating project folder: ' + directory))
        os.makedirs(directory)
        os.chdir(directory)


def find_link(url):
    end_url = url[::-1].find('/')
    root_url = url[:-end_url]

    try:
        web_page = urlopen(url).read() 
        web_page = web_page.decode('utf-8')
        print(green('Crawling link: ' + url))
    except HTTPError as err:
        if err.code == 404:
            print(red('Error 404 Not Found: ' + url))
        return []

    #use re.findall to get all the links
    links = []
    links = re.findall(r'(?<=href=")(.*?.html)[^"]*', web_page)
    web_scraper(web_page, url)

    full_links = []
    for link in links:
        if 'https://' not in link:
            full_links.append(root_url + link)
    return full_links


# Creates markdown file, and changes the html to markdown.
def web_scraper(web_page, url):
    end_url = url[::-1].find('/')
    root_url = url[:-end_url]
    
    filename = url.split("/")[-1]
    file_name = filename.replace('.html','.md')
    file = open(file_name, 'w+')

    seperated = web_page.split()
    web_page = " ".join(seperated)

    all_tags = '<h[1-6]>.*?</h[1-6]>|<img\s+src=\".*?>|<div\s+class=\"lead\">.*?</div>|<p\s+class=\"lead\">.*?</p>|<p>.*?</p>|<ul>.*?</ul>|<li>.*?</li>|<pre>.*?</pre>|<code>.*?</code>'
    tags = re.findall(all_tags, web_page)

    for lines in tags:
        if '<h1>' in lines:
            lines = lines.replace('<h1>','# ')
            lines = lines.replace('</h1>','\n')
        if '<h2>' in lines:
            lines = lines.replace('<h2>','## ')
            lines = lines.replace('</h2>','\n')
        if '<h3>' in lines:
            lines = lines.replace('<h3>','### ')
            lines = lines.replace('</h3>','\n')
        if '<pre>' in lines:
            lines = lines.replace('<pre>','\n````\n')
            lines = lines.replace('</pre>','\n````\n')
            lines = lines.replace('*','\n*')  
            lines = lines.replace('#','\n#') 
        if '<code>' in lines:
            lines = lines.replace('<code>','\n')
            lines = lines.replace('</code>','\n') 
            lines = lines.replace('&gt;','&gt;\n') 
        if '<li>' in lines:
            lines = lines.replace('<li>', '\n* ')
            lines = lines.replace('</li>', '')
            lines = lines.replace('<li> ', '\n* ')
        if '<ul>' in lines:
            lines = lines.replace('<ul>', '')
            lines = lines.replace('</ul>', ' \n\n')
        if '<p' in lines:
            lines = lines.replace('<p>', '')
            lines = lines.replace('</p>', '\n')
            lines = lines.replace('<p class="lead">', '> ')
        if '<div' in lines:
            lines = lines.replace('<div>', '')
            lines = lines.replace('</div>', '\n')
            lines = lines.replace('<div class="lead">', '')

        if '<img' in lines:
            first = lines.find('<img')
            last = lines.find('>')
            img_tag = lines[first:last+1]
            seperated = img_tag.split('"')
            for word in seperated:
                if '.png' in word:
                    if 'logo_python' in word:
                        lines = lines.replace(img_tag, '') 
                    else:
                        lines = lines.replace(img_tag, '\n![Picture link]('+root_url+ word +')\n\n') 
                if '.jp' in word:
                    lines = lines.replace(img_tag, '\n![Picture link]('+root_url+ word +')\n\n') 
                if '.JP' in word:
                    lines = lines.replace(img_tag, '\n![Picture link]('+root_url+ word +')\n\n') 

        if '<a' in lines:
            first = lines.find('<a')
            first_end = lines.find('>')
            last = lines.find('</a>')
            a_tag = lines[first:last+4]
            tag_seperated = a_tag.split('"')
            for word in tag_seperated:
                if 'http' in word:
                    lines = lines.replace(a_tag, '('+ word +')')
                if '.html' in word:
                    lines = lines.replace(a_tag, '('+root_url + word +')')
                if '#' in word:
                    lines = lines.replace(a_tag, '('+url + word +')')
        file.write(lines)
    file.close()


