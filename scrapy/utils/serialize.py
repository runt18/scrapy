import json
import datetime
import decimal

from twisted.internet import defer

from scrapy.http import Request, Response
from scrapy.item import BaseItem


class ScrapyJSONEncoder(json.JSONEncoder):

    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("{0!s} {1!s}".format(self.DATE_FORMAT, self.TIME_FORMAT))
        elif isinstance(o, datetime.date):
            return o.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(self.TIME_FORMAT)
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o, defer.Deferred):
            return str(o)
        elif isinstance(o, BaseItem):
            return dict(o)
        elif isinstance(o, Request):
            return "<{0!s} {1!s} {2!s}>".format(type(o).__name__, o.method, o.url)
        elif isinstance(o, Response):
            return "<{0!s} {1!s} {2!s}>".format(type(o).__name__, o.status, o.url)
        else:
            return super(ScrapyJSONEncoder, self).default(o)


class ScrapyJSONDecoder(json.JSONDecoder):
    pass
