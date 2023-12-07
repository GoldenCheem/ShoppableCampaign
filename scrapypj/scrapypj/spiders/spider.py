import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["shoppable-campaign-demo.netlify.app"]
    start_urls = ["https://shoppable-campaign-demo.netlify.app/#/"]

    def parse(self, response):
        pass
