# -*- coding: utf-8 -*-
"""
Created on Fri Sep 06 19:52:17 2013

@author: lanbing510
"""

import cgi
import papers_tool
from papers_tool import *

def proc_papers():
    print "Content-type: text/html\n" 
    reshtml="""
    <HTML>
    <HEAD><TITLE>
    CVPAPERS_TOOL
    </TITLE></HEAD>
    <BODY>
    </BODY>
    </HTML>"""

    form=cgi.FieldStorage()
    url=form['url'].value
    keywords=form['keywords'].value
    despool=loadUrl(url)
    keylistpool=simplifyPapers(despool,keywords)
    return despool,keylistpool

def printPapers(despool,keylistpool):
    for i in range(len(keylistpool)):
        print """<li><p>"""
        print """<font style="font-family: Arial;" size="-1">"""
        print despool[keylistpool[i][0]][0]
        for o in range(len(despool[keylistpool[i][0]][1])):
            pahtml="""[<a href="%s">%s</a>] """
            print pahtml % (despool[keylistpool[i][0]][1][o][1],despool[keylistpool[i][0]][1][o][0][0])
        print """<input type="checkbox" name="fruit" value ="apple" ><br></li>"""
        #print """"""

despool,keylistpool=proc_papers()
printPapers(despool,keylistpool)
shtml=  """
        <font style="font-family: Arial;" size="-1">
        <P>
        <hr>
        <P>
        Total Papers: %s &nbsp; &nbsp; &nbsp; &nbsp; Revelant Papers: %s<P>
        """
print shtml % (len(despool),len(keylistpool))
