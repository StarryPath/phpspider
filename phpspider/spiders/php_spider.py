import scrapy
import MySQLdb.cursors



from phpspider.items import PhpspiderItem
class phpSpider(scrapy.Spider):
    name = "phpspider"



    def __init__(self,category=None,*args,**kwargs):
        super(phpSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["%s" % category]





    def parse(self, response):


            item=PhpspiderItem()

            item['title'] = response.xpath('/html/head/title').re(u'[\u4e00-\u9fa5]')
            item['head'] = response.xpath('/html/head').re(u'[\u4e00-\u9fa5]')
            item['body'] =response.xpath('/html/body').re(u'[\u4e00-\u9fa5]')
            item['body']=  ''.join(item['body'])
            item['head'] = ''.join(item['head'])
            item['title'] = ''.join(item['title'])


            yield item



