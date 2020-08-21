import scrapy
import os

class AppstoreSpider(scrapy.Spider):
    name = 'appstore'
    allowed_domains = ['apple.com']
    start_urls = ['https://apps.apple.com/us/genre/ios/id36/']
    dirname = os.path.dirname(__file__)
    screenshots_dir = os.path.join(dirname, 'screenshots')

    custom_settings = {
        'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
        'IMAGES_STORE': screenshots_dir
    }

    def parse(self, response):
        category_links = response.xpath("//a[contains(concat('     ',normalize-space(@class),' '),' top-level-genre ')]")
        urls = []
        for link in category_links:
            url = link.css('a::attr(href)').extract_first()
            category = link.xpath('./text()').extract_first()
            cat = {
                "url": url,
                "category": category
            }
            yield cat
            urls.append(url)

        for next_url in urls:
            yield scrapy.Request(response.urljoin(next_url), callback = self.parse_popular)

    def parse_popular(self, response):
        lis = response.css("#selectedcontent ul li")
        urls = []
        for li in lis:
            url = li.css('a::attr(href)').extract_first()
            urls.append(url)

        for next_url in urls:
            yield scrapy.Request(response.urljoin(next_url), callback = self.parse_app)

    def parse_app(self, response):
        imgs = response.css('.we-screenshot-viewer__screenshots img')
        image_urls = imgs.css('img::attr(src)').extract()
        yield { 'image_urls': image_urls}