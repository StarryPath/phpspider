from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5

import MySQLdb
import MySQLdb.cursors


class PhpspiderPipeline(object):

    def __init__(self):
        try:
            self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host='localhost',
                                            db='test',
                                            user='root',
                                            passwd='',
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=True
                                            )
            print "Connect to db successfully!"

        except:
            print "Fail to connect to db!"

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):

        conn.execute('insert into biao2(title,head,body) values("%s","%s","%s")', (

            item['title'], item['head'],item['body']
        ))
