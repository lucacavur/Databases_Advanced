How to use this scraper

--packages to import
import requests
from bs4 import BeautifulSoup
import logging
import time

--
a function will run that will store the 4 variables into a logfile every 60 seconds

--important note
I understood this assignment as if once every minute, the URL needed to be scraped and the variables changed.
Later, I heard from fellow students that the page needed to be scraped nonstop. There was not enough time to change the code. 
I understood it this way, because of this specific sentence in the assignment which I understood wrongly:
  "Make sure your scraper works in realtime! That is to say: once I run your scraper, it should keep scraping for every minute it is running until I close it."
 Apologies! 
