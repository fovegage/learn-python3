# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyspiderPipeline(object):

    def __init__(self):
        self.file = open('techer.txt', 'w')

    # 必须实现且必须返回
    def process_item(self, item, spider):
        # content = json.dumps(dict(item)) + "\n"
        content = str(item) + '\n'
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()