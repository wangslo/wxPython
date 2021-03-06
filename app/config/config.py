# coding:utf-8
import pymysql


class Config(object):

    @staticmethod
    def database():
        return dict(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="root",
            db="spider",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
