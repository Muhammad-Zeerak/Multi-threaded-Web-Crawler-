Web Crawler
 
I.	INTRODUCTION 
A.	Main Sketch:
Web crawler will follow the following steps to crawl a web URL:
1)	Parse the required HTML page and find all the strings which match a typical "URL" pattern.
2)	The first set of URLs are put in a file called "queueList.txt".
3)	After that, the contents of the queue are pulled out:
a.	They are put in a set and the whole process is repeated till there are no more URLs.
b.	Each of the crawled URLs which belong to the same domain name are put in a final file, "crawledList.txt".
4)	The process is sped up using multithreading.
5)	The threads are always in order because we added semaphores from the library threading.

B.	Speeding up the process:
In general, as far as computational time is concerned, writing into a file takes a considerably good amount of time. In general, when we are trying to crawl over a huge page, this can come into as a difficulty and then, you can observe the noticeable time lag. We can use a set.
So, Suppose there are 30 URLs in our waiting list, which are needed to be crawled. Instead of reading and writing contents from the file (queue.txt) every time, we use a set. We convert the elements of the file into set items and access them through the set.

C.	Getting Links:
We need to parse the html and find the links in each page. Python comes with a built-in HTMLParser class which has all the features necessary to implement the same.
Say we have some URL like this:
 
We need to parse HTML page and find the tag which begins with 'a' and extract only the 'href' attribute's value.
We have the base URL already extracted and stored. We just need to join the subsequent URL with the base and make it the final URL. The code snippet for getting links is:
 

II.	IMPLEMENTING CRAWLER
A.	Crawler Function:
The crawler is responsible for connecting to the consequent pages and crawl through them in order.
1)	There is a waiting list(queue.txt) containing a bunch of URLs.
2)	The crawler grabs the first URLs from the waiting list and connects to it and grab all of its HTML.
3)	It then calls in the link_finder program.
4)	The link finder will do its thing: parse through the HTML and return the set of URLs
5)	Once the crawler has all the URLs or links, it is going to add them to the waiting list.
6)	Another thing which it is going to do, is move the crawled pages from the waiting list to the crawled list. That way, we make sure we do not crawl the same page twice. 


IV.	OBSERVATIONS AND CONCLUSION
Our web crawler is successfully able to crawl:
1.	Open websites_ websites without any security to stop the crawler to crawl the pages.
2.	Unrestricted Websites
For Example: https://lms.nust.edu.pk/ 
In this case, most of the links were crawled. We ended up with a total of 35 links. 
Finally, I can also say, this is quite a fast crawler. It crawled 35 links in merely 40 seconds or so. 
There are and always will be some HTTP Errors. But that's because those pages are dead now or there is some kind of a server error. e.g., HTTP Error 403, 404 etc.

