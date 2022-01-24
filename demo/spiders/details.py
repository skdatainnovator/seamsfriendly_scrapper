#Importing Neccessary Libraries
import scrapy
import pandas as pd 

class detailsSpider(scrapy.Spider):
    name = 'details'

    def start_requests(self):
        #To get all the links of the Shorts
        df = pd.read_csv('C:/Users/Sourav Kumar/VScodeProjects/programming_test/scrapy_artyvis/demo/links.csv')
        link = df['link'].to_list()
        for url in link:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        #To get the name , img_url , price , desc of the shorts

        name = response.xpath("//h1/text()").extract()[0].replace('\n','')
        img_urls = response.xpath("//div[@class = 'AspectRatio AspectRatio--withFallback']/img [@class = 'Image--lazyLoad Image--fadeIn']").xpath('@data-original-src').extract()

        desc = ('').join(response.xpath("//div[@class = 'ProductMeta__Description']/div[@class = 'Rte']/p/text()").extract()[0:3]).replace('All products shown in this picture, apart from these Shorts, are purely for Styling and Photography purposes. These will not be included in your order.','')

        price = response.xpath("//div[@class = 'Heading']/span [@class = 'ProductMeta__Price Price  u-h4']/text()").extract()[0]

        df = pd.read_csv('C:/Users/Sourav Kumar/VScodeProjects/programming_test/scrapy_artyvis/demo/details.csv')

        list_detail = [name,img_urls,price,desc]

        df.loc[len(df)] = list_detail
        #save the data
        df.to_csv('C:/Users/Sourav Kumar/VScodeProjects/programming_test/scrapy_artyvis/demo/details.csv',index=False)




