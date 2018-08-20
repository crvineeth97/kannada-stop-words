from scrapy.spiders import Rule, CrawlSpider
from crawler.items import CrawlerItem
from urllib.parse import urlparse
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import scrapy
import re

class MySpider(CrawlSpider):
    name = "udayavani"
    allowed_domains = ["udayavani.com"]
    start_urls = ["http://www.udayavani.com/kannada/category/bollywood-news", "http://www.udayavani.com/kannada/category/balcony-sandalwood-news", "http://www.udayavani.com/kannada/category/interviews", "http://www.udayavani.com/kannada/category/state-news", "http://www.udayavani.com/kannada/category/sports-news", "http://www.udayavani.com/kannada/category/national-news", "http://www.udayavani.com/kannada/category/world-news", "http://www.udayavani.com/kannada/category/business-news", "http://www.udayavani.com/kannada/category/tech-world"]


    rules = (

        Rule(
            LxmlLinkExtractor(restrict_xpaths=("//div[@id='block-system-main']",)),
            callback='parse_article',
            process_links='link_filtering',
            follow=True
        ),

    )

    def parse_article(self, response):
        main = response.xpath('//div[@id="main-content"]')
        title = main.xpath('//h1[@id="page-title"]/span/text()').extract()
        content =  main.xpath('//div[@class="field-item even"]/p').extract()
        item = CrawlerItem()
        if len(content) == 0:
            return
        item["url"] = response.url
        item["content"] = []
        cleanr = re.compile('<.*?>')
        for c in content:
            if len(c) > 1:
                c = re.sub(cleanr,'', c).replace('\n','')
                item["content"].append(c)
        
        count = 0
        for line in item["content"]:
            count+=len(line.split())
        if count < 500:
            # print(count)
            return
        
        item["title"] = title[0].replace('<', '').replace('>', '').replace(':', '').replace('"', '').replace('/', '').replace('|', '').replace('*', '').replace('?', '')
        return item

    def link_filtering(self, links):
        ret = []
        for link in links:
            if "kannada" in link.url:
                ret.append(link)
        return ret
