# -*- coding: utf-8 -*-
"""
Created on Fri Sep 06 12:52:17 2013

@author: lanbing510
"""

import re
import urllib2
from BeautifulSoup import BeautifulSoup


def readBuf(fsrc, length=16*1024):
    """解决一次性读取时出现的 self._sock.recv(left) error:[Errno 10054],分批读取并最后返回数据"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        return buf


def loadUrl(url="http://www.cvpapers.com/cvpr2013.html"):
    full_url=url
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',\
    'Host':'www.cvpapers.com'}
    request=urllib2.Request(full_url,headers=headers)
    response=urllib2.urlopen(request)
    response=readBuf(response)

    soup=BeautifulSoup(response)
    pool=soup.findAll('dt')
    despool={}
    index=0
    for pl in pool:
        item=[]
        paper_name=pl.contents[0]
        paper_name=paper_name.strip('(')
        paper_url=[]
        pul=pl.findAll('a')
        for i in range(len(pul)):
            paper_url.append((pul[i].contents,pul[i].get('href')))
        item=[paper_name,paper_url]
        dl={index:item}
        despool.update(dl)
        index+=1
    return despool

def simplifyPapers(despool,keywords):
    keywords=keywords.split()

    #开始查找
    keydicpool={} #存放含有关键字的条目和相应含有的个数(供相关性排序)
    for i in range(len(despool)):
        includekey=[]
        for kd in keywords:
            p=re.compile(kd,re.IGNORECASE)
            r=p.search(despool[i][0])
            if r is not None:includekey.append(r.group())
            if len(includekey)!=0:
                dl={i:len(includekey)}
                keydicpool.update(dl)
        
    #keylistpool=sorted(keydicpool.items(),key=lambda d:d[0],reverse=True)  
    keylistpool=sorted(keydicpool.items(),key=lambda d:d[1],reverse=True)
    return keylistpool
    
def printResult(despool,keylistpool):
    print 'total number of the revelant papers is %d \n'% len(keylistpool)
    for i in range(len(keylistpool)):
        print '<',despool[keylistpool[i][0]][0],'>','\n'
        

if __name__=='__main__':
    despool=loadUrl()
    keywords=raw_input()
    keylistpool=simplifyPapers(despool,keywords)
    printResult(despool,keylistpool)
