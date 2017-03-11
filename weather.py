#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import urllib2
import sys

api_key = None


class WeatherHourly(object):

    url_base = "http://api.wunderground.com/api/"
    url_service = {
        "hourly": "/hourly/q/CA/"
    }

    def __init__(self, api_key):
        super(WeatherHourly, self).__init__()
        self.api_key = api_key

    def hourly(self, location):
        url = WeatherHourly.url_base + self.api_key + \
            WeatherHourly.url_service["hourly"] + location + ".xml"

        # Llegir la url
        fitxer = urllib2.urlopen(url)
        data = fitxer.read()
        fitxer.close()

        return data


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
            # hora =  raw_input("Escriu les hores:")
        except IndexError:
            print "API key must be in CLI option"

    wc = WeatherHourly(api_key)
    resultat = wc.hourly("Lleida")
    print resultat
