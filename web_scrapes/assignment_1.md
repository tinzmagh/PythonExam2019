Assignment 1
# Crawl a web site and save the content in markdown

![Picture link](https://clbokea.github.io/exam/src/main-qimg-c224920a6f3ae3f8089ccd1e8dad65af.jpeg)

Choose a website of your own choice or use (https://clbokea.github.io/exam/index.html) crawl it and "scrape" it.
The content of the website should be saved in markdown formatted files on your computer.
It can be a good idea to choose a relatively small website.
It can also be a good idea to have some sort of limit on which links you want to follow. 
What you choose to retrieve from the crawled site is up to you. But you should describe why you choose to do like you did.
## An Example
A html page looking like this:

````
 
 &lt;!DOCTYPE html&gt;
 &lt;html lang="en"&gt;
 &lt;head&gt;
 &lt;meta charset="UTF-8"&gt;
 &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
 &lt;meta http-equiv="X-UA-Compatible" content="ie=edge"&gt;
 &lt;link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"&gt;
 &lt;title&gt;
Index&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;nav class="nav"&gt;
 &lt;a class="nav-link active" href="index.html"&gt;
Home&lt;/a&gt;
 &lt;a class="nav-link" href="about.html"&gt;
About&lt;/a&gt;
 &lt;a class="nav-link" href="contact.html"&gt;
Contact&lt;/a&gt;
 &lt;/nav&gt;
 &lt;div class="container"&gt;
 &lt;h1&gt;
Clbo company&lt;/h1&gt;
 &lt;p&gt;
Welcome home!&lt;/p&gt;
 &lt;p&gt;
Here you have a list of our services&lt;/p&gt;
 &lt;ul&gt;
 &lt;li&gt;
Web Scraping&lt;/li&gt;
 &lt;li&gt;
Web Design&lt;/li&gt;
 &lt;li&gt;
Backend development&lt;/li&gt;
 &lt;/ul&gt;
 &lt;/div&gt;
 &lt;/body&gt;
 &lt;/html&gt;
 
 
````
Becomes:

````
 
# Clbo company Welcome home! Here you have a list of our services 
* Web Scraping 
* Web Design 
* Backend development 
````
The links to follow (crawl) would in this case be "about.html" and "contact.html"
