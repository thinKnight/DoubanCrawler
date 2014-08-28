# -*- coding: UTF-8 -*-
import re 
import urllib2

def douban_crawler(url_head, target):
    for page in range(0, 1000, 20):

        url_rear = "?start=%d&type=T" % page
        url_use = url_head + url_rear

        content = urllib2.urlopen(url_use).read()
        content = content.decode("UTF-8").encode("UTF-8")

        content = content.replace(r'title="去FM收听"', "")
        content = content.replace(r'title="去其他标签"', "")

        name = re.findall(r'title="(\S*?)"', content, re.S)
       
        num  = re.findall(r'<span\s*class="rating_nums">([0-9.]*)<\/span>', content)

        
        doc = zip(name, num)
        
        if target == "book":
            dou = open("doc_book", 'a')
        elif target == "music":
            dou = open("doc_music", 'a')
        elif target == "movie":
            dou = open("doc_movie", 'a')

        for i in doc:
            dou.write(i[0] + " " + i[1] + "\n")
            
    dou.close()

if __name__ == '__main__':
    target = raw_input("豆瓣 book movie music，你想爬哪一个? ")

    tag   = raw_input("请输入你想要检索的标签: ")

    url_head  = "http://%s.douban.com/tag/%s" % (target, tag)

    douban_crawler(url_head, target)

































