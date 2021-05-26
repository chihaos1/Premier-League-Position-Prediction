import scrapy
from myproject.items import LeagueTableItem
from scrapy.loader import ItemLoader

class LeagueTableSpider(scrapy.Spider):
    name = 'league_table'
    
    COUNT_MAX = 27
    count = 0

    start_urls = [
        'https://en.wikipedia.org/wiki/1992%E2%80%9393_FA_Premier_League'
    ]
    
    def parse(self, response):
        for league_table in response.xpath('//table[@class="wikitable"][2]'):
            for i in range(20):
                l = ItemLoader(item=LeagueTableItem(), selector=league_table)
                l.add_xpath('Team', f"//*[@class='wikitable']/tbody/tr[{i+2}]/th[contains(@scope, 'row')]/a")
                l.add_xpath('Position', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][1]")
                l.add_xpath('Points', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][9]")
                l.add_xpath('Played', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][2]")
                l.add_xpath('Goal_Deficit', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][8]")
                l.add_xpath('Goal_Against', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][7]")
                l.add_xpath('Goal_For', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][6]")
                l.add_xpath('Lost', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][5]")
                l.add_xpath('Drawn', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][4]")
                l.add_xpath('Won', f"//*[@class='wikitable']/tbody/tr[{i+2}]/td[contains(@style, 'font')][3]")
                
                yield l.load_item() 

        next_page = response.xpath('//div[@style="float: right;"]/a/@href').extract_first()
        if self.count < self.COUNT_MAX:
            next_page_link = response.urljoin(next_page)
            self.count+=1
            yield scrapy.Request(url=next_page_link, callback=self.parse)