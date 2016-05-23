
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from rss.items import RssItem
import feedparser

def get_domains():
    lines = open('rss/misc/popular.txt', 'r').readlines()
    domains = [line.strip() for line in lines]
    urls = ['http://{0}'.format(domain.strip()) for domain in domains]
    return domains, urls

class RssSpider(CrawlSpider):
    name = 'rss'
    allowed_domains, start_urls = get_domains()

    rules = (
        Rule(LinkExtractor(allow=('.*', )), callback='parse_item'),
    )

    def __init__(self, domain=None, *args, **kwargs):
        super(RssSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://{0}'.format(domain)]

    def parse_article(self):
        pass

    def parse_item(self, response):

        try:
            page = feedparser.parse(response.body)
            if page.bozo == 0:
                print response.url
                item = RssItem()
                item['url']
                yield item
        except:
            pass
