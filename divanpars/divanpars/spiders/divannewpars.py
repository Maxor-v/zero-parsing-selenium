import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
       lamps = response.css('div.LlPhw')
       for lamp in lamps:
         yield {
           # Ссылки и теги получаем с помощью консоли на сайте
           # Создаём словарик названий, используем поиск по диву, а внутри дива — по тегу span
           'name' : lamp.css('div.lsooF span::text').get(),
           # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
           'price' : lamp.css('div.pY3d2 span::text').get(),
           # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
           # Атрибуты — это настройки тегов
           'url' : lamp.css('a').attrib['href']
           }