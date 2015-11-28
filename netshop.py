#!/usr/bin/env python
#coding=utf-8 

import httplib

class Member:
    id=0
    name=''
    soldout=False
    
    def __init__(self,id,name):
        self.id=id
        self.name=name

class NetshopPhoto:
    start=0
    end=0
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.conn = httplib.HTTPConnection("shopping.akb48-group.com")  
        
    def check(self,id):
        self.conn.request('GET', '/products/detail.php?product_id=%d'%id)
        r = self.conn.getresponse()
        if r.status!=200: return
        t=r.read()
        p=re.compile(ur'5Ã¶¥»¥Ã¥È\s+([^\s]+)\s')
        m=p.search(t)
        if m:
            name=m.group(1)
            print name
        if t.find('soldout')>0:
            soldout=True
            print 'Sold Out!'
        return
        
nsp=NetshopPhoto(35174,35255)
nsp.check(35174)