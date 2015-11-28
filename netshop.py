#!/usr/bin/env python
#coding=utf-8 

import httplib
import re

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
        t=t.decode('utf-8','ignore')
        p=re.compile(ur'5枚セット ([^|]+)\s')
        m=p.search(t)
        if m:
            name=m.group(1)
        else:
            print 'not found'
            return
        #print 
        if t.find('soldout')>0:
            soldout=True
            #print 'name='+name+': Sold Out!'
        else:
            print name+' ',
        return
    def doit(self):
        i=self.start
        while i<=self.end:
            self.check(i)
            i=i+1
        
nsp=NetshopPhoto(35174,35255)
#nsp.check(35174)
nsp.doit()