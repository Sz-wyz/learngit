#程序的开始文件
from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider'.split())