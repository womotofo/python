# -*- coding: UTF-8 -*-
import datetime
from urllib import request
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = 'https://petitions.whitehouse.gov/'
    req = request.Request(url)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    # 创建Beautiful Soup对象
    soup = BeautifulSoup(html, 'lxml')
    tag = soup.find(attrs={"data-nid": "2545476"})
    count = tag.find("span", attrs={"class": "signatures-number"}).string
    now = datetime.datetime.now()
    dead_line = datetime.datetime.strptime(
        '2017-06-18', '%Y-%m-%d')
    delta = dead_line - now
    per = (30 - delta.days) / 30 * 100
    print("  all_count : %s" % count)
    print("remain_days : %d" % delta.days)
    print("    percent : %.2f%%" % per)
