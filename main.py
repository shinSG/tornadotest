#!/usr/bin/python
# encoding: utf-8

from tornado import ioloop
from tornado import web
from testobj import t


class BaseHandler(web.RequestHandler):
    def __init__(self, *args, **kwargs):
        self.flag = {}
        super(BaseHandler, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def post(self, *args, **kwargs):
        raise NotImplementedError


class T1Handler(BaseHandler):
    def get(self, *args, **kwargs):
        print self.flag
        self.flag = {
            'name': 'test1'
        }
        t.a()
        self.write(self.flag)


class T2Handler(BaseHandler):
    def get(self, *args, **kwargs):
        print self.flag
        self.flag = {
            'name': 'test2'
        }
        t.a()
        self.write(self.flag)


url_router = [
    (r'/t1', T1Handler),
    (r'/t2', T2Handler),
]


if __name__ == '__main__':
    app = web.Application(handlers=url_router)
    app.listen(8888)
    ioloop.IOLoop.current().start()
