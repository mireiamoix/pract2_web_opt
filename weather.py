#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import urllib2
import sys
from bs4 import BeautifulSoup

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

        soup = BeautifulSoup(data, 'lxml')
        forecast = soup.find_all("forecast")

        max_hores = proximes_hores
        j = 0
        for i in forecast:
            if j >= int(max_hores):
                break

            hora = "A les " + i.find("hour").text
            temperatura = " la temperatura sera " + i.find("temp").find("metric").text
            sensacio_temp = ". Pero amb una sensacio termica de " + (i.find("feelslike").find("metric").text)
            cel = " i amb un cel " + i.find("wx").text
            print hora + temperatura + sensacio_temp + cel

            j = j+1


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
            proximes_hores = raw_input("Escriu el numero de les hores que vols saber la prediccio: ")
        except IndexError:
            print "API key must be in CLI option"

    print "Es tindra una prediccio de les proximes " + proximes_hores + " hores."
    wc = WeatherHourly(api_key)
    wc.hourly("Lleida")
