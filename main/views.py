from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from daylifenews.DayLifeAPI.DayLifeAPI import DaylifeAPI
from daylifenews.settings import *

def get_content(topic):
    import time
    api_instance = DaylifeAPI(** DAYLIFE_ARGS)
    now = long(time.time())
    weekago = now - (7*86400)
    params = {'query':topic, 'start_time':weekago, 'end_time':now, 'sort':"date"}
    search = api_instance.search_getRelatedArticles(**params)
    articles = search[u'response'][u'payload'][u'article']  
    keys = ['headline', 'timestamp', 'excerpt', 'source', 'url']
    content = [ dict((key, article[key]) for key in keys) for article in articles ]
    return { 'topic':topic, 'content': content }

def main_view(request):
    template_name = "main/main.html"
    if len(DAYLIFE_ARGS) :
        topics = ["Iran", "General Motors", "Apple"]
        content = [get_content(topic) for topic in topics]
    else:
        content = None
    news = { 'news': content }
    return render_to_response(template_name, news, context_instance=RequestContext(request))
