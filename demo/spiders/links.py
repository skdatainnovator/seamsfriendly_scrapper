#importing necessary libraries
import scrapy
import pandas as  pd


class linkSpider(scrapy.Spider):
    name = "get_link"

    def start_requests(self):
        #url of the list of shorts
        urls = [
            'https://in.seamsfriendly.com/collections/shorts','https://in.seamsfriendly.com/collections/shorts?page=2','https://in.seamsfriendly.com/collections/shorts?page=3'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url[-1]

        links = []
        domain = 'https://in.seamsfriendly.com/'
        df = pd.read_csv('links.csv')
        for i in range(len(response.css("h2").xpath("a"))):
            link = domain+response.css("h2").xpath("a")[i].xpath("@href").extract()[0] 
            links.append(link)
        df2 = pd.DataFrame(links , columns=['link'])

        pd.concat([df,df2]).to_csv('links.csv',index=False)

        self.log(f'Total No of page extarcted link = {page}')
