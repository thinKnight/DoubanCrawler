# -*- coding: UTF-8 -*-
# 如果要在python2的py文件里面写中文，则必须要添加一行声明文件编码的注释，否则python2会默认使用ASCII编码。  

import re 
import urllib2

def douban_crawler(url_head, target):
    for page in range(0, 1000, 20):
    #这个1000是检索的条目数量，可以按需设定
        url_rear = "?start=%d&type=T" % page
        url_use = url_head + url_rear
        #两段合成真正的url
        content = urllib2.urlopen(url_use).read()
        content = content.decode("UTF-8").encode("UTF-8")
        
        content = content.replace(r'title="去FM收听"', "")
        content = content.replace(r'title="去其他标签"', "")
        
        name = re.findall(r'title="(\S*?)"', content, re.S)
        #正则表达式捕获标题
        num  = re.findall(r'<span\s*class="rating_nums">([0-9.]*)<\/span>', content)
        #正则表达式捕获分数
        
        doc = zip(name, num)
        #将标题和分数打包成([ , ][ , ]...)的形式
        if target == "book":
            dou = open("doc_book.txt", 'a')
        elif target == "music":
            dou = open("doc_music.txt", 'a')
        elif target == "movie":
            dou = open("doc_movie.txt", 'a')

        for i in doc:
            dou.write(i[0] + " " + i[1] + "\n")
            #写入
    dou.close()

if __name__ == '__main__':
    target = raw_input("豆瓣 book movie music，你想爬哪一个? ")

    tag   = raw_input("请输入你想要检索的标签: ")

    url_head  = "http://%s.douban.com/tag/%s" % (target, tag)

    douban_crawler(url_head, target)
    
    print "抓取完毕"































