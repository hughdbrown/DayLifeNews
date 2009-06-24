from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from daylifenews.DayLifeAPI.DayLifeAPI import DaylifeAPI
from daylifenews.settings import *

import time

def main_view(request):
    template_name = "main/main.html"
    if len(DAYLIFE_ARGS) :
        d = DaylifeAPI(** DAYLIFE_ARGS)
        now = long(time.time())
        weekago = now - (7*86400)
        params = {'query':"Iran", 'start_time':weekago, 'end_time':now, 'sort':"date"}
        context = d.search_getRelatedArticles(**params)
    else:
        context = None
    return render_to_response(template_name, context, context_instance=RequestContext(request))
