from django.urls import path
from inec_webapp.views import *

urlpatterns = [
	path('', pollIndex, name='home'),
	path('polling_unit/list', pollList, name='poll_list'),
	path('polling_unit/detail', pollDetail, name='poll_detail'),
	path('create_poll/', createPoll,name='create_poll')
]