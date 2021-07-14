from django.urls import path

from . import views

urlpatterns = [
    # our-domain.com/meetups/
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>/success', views.confirm_registration,
         name='confirm_registration'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]
