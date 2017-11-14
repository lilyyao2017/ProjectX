import scrapy
import os
import csv

class CaixinSpider(scrapy.Spider):
  """Customized spider class for scrawling from 
  http://china.caixin.com/anticorruption/.

  This implementation is based on the base skeleton of scrapy.Spider. See
  http://china.caixin.com/anticorruption/ for the tutoriol.
  """

  # Name of the spider
  name = "caixins"

  # Starting point of the crawling
  # The spider fetches the following pages and stores the returned content in
  # the 'response' object to be parsed by the method below.
  start_urls = [
      'http://china.caixin.com/anticorruption-list/',
  ]

  def parse(self, response):
    """ Method that actually parses the responded page
    
    The response is stored in HtmlResponse and can be manipulated using the 
    scrapy.selectors. See https://doc.scrapy.org/en/latest/topics/selectors.html
    
    FYI: The response is same as what a browser gets when it fetches the 
    same page. The raw format (html) of the page can be viewed by clicking 
    'inspect element' in a browser.
    """        
    
    # Output file to save the results
    filepath = CaixinSpider.name + '.csv'
    separator = '|'  # use '|' as the separator
    # Open the file in 'appending' mode. If the file does not exist, write 
    # element titles in the first line.
    if os.path.isfile(filepath):
      ofile = open(filepath, 'a+')
      writer = csv.writer(ofile, delimiter=separator)
    else:
      ofile = open(filepath, 'a+')
      writer = csv.writer(ofile, delimiter=separator)
      writer.writerow(['TITLE', 'DATE', 'DESCRIPTION', 'LINK'])    
    
    # [Fan Fu Zhou Ji]s
    # They're stored in a 'div' element whose class attribute has value 
    # 'stitXtuwen_list'
    weekly_items = response.selector.xpath(
        '//div[contains(@class,"stitXtuwen_list")]/dl/dd')

    # For each item, extract its title, date, description and link respectively
    # The <dd> element is in the following format:
    # <dd>
    #   <h4>
    #     <a href="link"> TITLE </a>
    #     <span> DATE </span>
    #     <p> DESCRIPTION </p>
    #   </h4>
    # </dd>
    for item in weekly_items:
      # a/text() gets the content of tag 'a'
      title = item.xpath('h4/a/text()')[0].extract().encode('utf-8')     
      # a/@href gets the value of attribute 'href' of tag 'a'
      link = item.xpath('h4/a/@href')[0].extract().encode('utf-8')
      date = item.xpath('span/text()')[0].extract().encode('utf-8')
      description = item.xpath('p/text()')[0].extract().encode('utf-8')
      
      # Write this item into the file
      writer.writerow([title, date, description, link])    
      #ofile.write(title)
      #ofile.write(separator)
      #ofile.write(date)
      #ofile.write(separator)
      #ofile.write(description)
      #ofile.write(separator)
      #ofile.write(link)
      #ofile.write(separator)
      #ofile.write('\n') # newline
    
    ofile.close()

    print '------------------'
    print '---- SUCCESS! ----'
    print '------------------'

    
