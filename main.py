import threading
from queue import Queue
from crawler import Crawler
import fileManipulation as files
import time
from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split(".")
        return results[-2] + '.' + results[-1] #only the last 2 items of the results list
    except:
        return ''

# Get the subdomain name (name.example.com)
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc # parse through the given url and return the network location (netloc)
    except:
        return '' # since we need to return something!

project_name = input("Enter the project name: ")
home_page = input("Enter the homepage URL: ")
threads = input("Enter number of threads: ")
threads = int(threads)

DOMAIN_NAME = get_domain_name(home_page)
QUEUE_FILE = project_name + '/queueList.txt'
CRAWLED_FILE = project_name + '/crawledList.txt'
NUMBER_OF_THREADS = threads
queue = Queue()


# The first spider instance does not need a multithreaded approach.
# We just need to find generate the first queue of urls from the base_url or the home page.
Crawler(project_name, home_page, DOMAIN_NAME)


# Creating Threads (The threads will die after main terminates)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True # which suggests that the threads are left as main terminates
        t.start()

# Do the next job in the queue
# Essentially iterate through the queue and take each url and crawl it
# runs the threads in order due to semaphores
sem = threading.Semaphore() #for semaphores
def work():
    while True:
        sem.acquire()
        url = queue.get()
        Crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()
        sem.release()
        time.sleep(0.25)


# Basically each queued_link is a new job
def create_jobs():
    for link in files.file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join() # to avoid collision among multiple threads
    crawl()


# iterating through the queue and checking if any urls are left
# if so then crawl them until the whole queue is empty
def crawl():
    queued_links = files.file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print('Total of ' + str(len(queued_links)) + ' links extracted in the queue. Crawling them 1 by 1 now....')
        create_jobs()

create_workers()
crawl()
