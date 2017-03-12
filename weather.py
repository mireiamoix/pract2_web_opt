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
        j = 0  # variable per controlar les hores que es volen

        for i in forecast:  # tantes voltes com max_hores passades
            if j >= int(max_hores):
                break

            hora = "A les " + i.find("hour").text
            temperatura = " la temperatura sera " + i.find("temp").find("metric").text
            sensacio_temp = (i.find("feelslike").find("metric").text)
            sensacio_temp_frase = ". Pero amb una sensacio termica de " + sensacio_temp
            cel = i.find("wx").text
            cel_frase = " i amb un cel " + cel
            print hora + temperatura + sensacio_temp_frase + cel_frase

            if (cel == "Mostly Clear" or cel == "Clear" or cel == 'Sunny' or cel == "Mostly Sunny"):
                if (int(sensacio_temp) > 22):
                    print "  CONSELL: si portes jaqueta et sobrara.\n"
                print "  CONSELL: pots portar jaqueta per si refresca.\n"

            if (cel == "Partly Cloudy" or cel == "Cloudy" or cel == "Rainy" or cel == "Mostly Rainy"):
                if int(sensacio_temp) > 25:
                    print "  CONSELL: Porta paraigües que ploura, pero jaqueta no cal.\n"
                print "  CONSELL: Porta paraigües i jaqueta per si refresca.\n"

            j = j+1


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
            proximes_hores = raw_input("Escriu el numero de les hores que vols saber la prediccio: ")
        except IndexError:
            print "API key must be in CLI option"

    print "Es tindra una prediccio de les proximes " + proximes_hores + " hores.\n"
    wc = WeatherHourly(api_key)
    wc.hourly("Lleida")
