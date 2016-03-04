#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016/3/4 10:30

@author: sodbvi
'''
import datetime
from django.http import HttpResponse,Http404
from django.template import  Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now=datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)

#代码中使用模版
#    t=Template("<html><body>It is now {{ current_date }}.</body></html>")
#    html=t.render(Context({'current_date':now}))
#    return HttpResponse(html)

#方式1从文件系统输入模版
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

#方式2从文件系统输入模版
#    return render_to_response('current_datetime.html', {'current_date': now})

#方式3从文件系统输入模版
    return render_to_response('mypage.html', {'current_section': 'my section','title':'my title'})

def extends_current_datetime(request):
     now=datetime.datetime.now()
     return render_to_response('extends/current_datetime.html', {'current_date':now })

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def extends_hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render_to_response('extends/hours_ahead.html', {'hour_offset': offset,'next_time':dt})