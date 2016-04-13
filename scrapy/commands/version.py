from __future__ import print_function
import sys
import platform

import twisted
import OpenSSL

import scrapy
from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):

    default_settings = {'LOG_ENABLED': False}

    def syntax(self):
        return "[-v]"

    def short_desc(self):
        return "Print Scrapy version"

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("--verbose", "-v", dest="verbose", action="store_true",
            help="also display twisted/python/platform info (useful for bug reports)")

    def run(self, args, opts):
        if opts.verbose:
            import lxml.etree
            lxml_version = ".".join(map(str, lxml.etree.LXML_VERSION))
            libxml2_version = ".".join(map(str, lxml.etree.LIBXML_VERSION))
            print("Scrapy    : {0!s}".format(scrapy.__version__))
            print("lxml      : {0!s}".format(lxml_version))
            print("libxml2   : {0!s}".format(libxml2_version))
            print("Twisted   : {0!s}".format(twisted.version.short()))
            print("Python    : {0!s}".format(sys.version.replace("\n", "- ")))
            print("pyOpenSSL : {0!s}".format(self._get_openssl_version()))
            print("Platform  : {0!s}".format(platform.platform()))
        else:
            print("Scrapy {0!s}".format(scrapy.__version__))

    def _get_openssl_version(self):
        try:
            openssl = OpenSSL.SSL.SSLeay_version(OpenSSL.SSL.SSLEAY_VERSION)\
                .decode('ascii', errors='replace')
        # pyOpenSSL 0.12 does not expose openssl version
        except AttributeError:
            openssl = 'Unknown OpenSSL version'

        return '{} ({})'.format(OpenSSL.version.__version__, openssl)
