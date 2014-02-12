from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import *
from django.template import RequestContext
from django.utils import simplejson
import socket 
import os
module_dir = os.path.dirname(__file__)  # get current directory

def ajax(request):
	if request.POST.has_key('client_response'):
		x = request.POST['client_response']
         
		y = 'Hello' + x
		
		response_dict = {} 		     
		response_dict.update({'server_response': y })                                                                  
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def index(request):
	return render_to_response('app/index.html')

