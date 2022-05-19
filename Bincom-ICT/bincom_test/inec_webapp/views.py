from django.shortcuts import render

# Create your views here.
def pollIndex(request):
	template_name = 'base.html'
	context = {
		'pl':'Poll-Unit-Home'
	}
	return render(request,template_name,context)

def pollList(request):
	template_name = 'inec_webapp/poll_list.html'
	context = {
		'pl':'Poll-Unit-Lists'
	}
	return render(request,template_name,context)

def pollDetail(request):
	template_name = 'inec_webapp/poll_detail.html'
	context = {
		'pl': 'Poll-Unit-Summary-For-Scores'
	}
	return render(request,template_name,context)

def createPoll(request):
	template_name = 'inec_webapp/vote_poll.html'
	context = {
		'pl': 'Votings'
	}
	return render(request,template_name,context)
