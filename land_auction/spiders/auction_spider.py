import scrapy
import os

class AuctionSpider(scrapy.Spider):
    name = 'auction_spider'
    # internet file
    start_urls = ['http://saas.qiyudata.com/dataQuery/3556']

    # local html file
    # project_root = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(project_root, '..', 'targeted_websites', 'qiyu_page.html')
    # start_urls = [f'file:///{file_path}']

    def parse(self, response):
        # 提取相关信息的XPath路径
        rows = response.xpath('//div[@class="ag-body-container ag-layout-normal"]/div[@role="row"]')

        for row in rows:
            yield {
                'LandCaption': row.xpath('.//div[@col-id="LandCaption"]/div/text()').get(),
                'UseType': row.xpath('.//div[@col-id="UseType"]/div/text()').get(),
                'DocumentIssueDate': row.xpath('.//div[@col-id="DocumentIssueDate"]/div/text()').get(),
                'BasePrice': row.xpath('.//div[@col-id="BasePrice"]/div/text()').get(),
                'Price': row.xpath('.//div[@col-id="Price"]/div/text()').get(),
                'BlockPrice': row.xpath('.//div[@col-id="BlockPrice"]/div/text()').get(),
                'Invisor': row.xpath('.//div[@col-id="Invisor"]/div/text()').get(),
                'ChangeDateTime': row.xpath('.//div[@col-id="ChangeDateTime"]/div/text()').get(),
            }
