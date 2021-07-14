from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from .models import Meetup, Participants
from .forms import RegistrationForm


def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):

    try:

        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        print(meetup_slug)
        print(selected_meetup)

        if request.method == 'GET':

            registrationForm = RegistrationForm()

        else:
            registrationForm = RegistrationForm(request.POST)

            if registrationForm.is_valid():
                user_email = registrationForm.cleaned_data['email']
                participanT, _ = Participants.objects.get_or_create(  # _ => was_created
                    email=user_email)
                selected_meetup.participant.add(participanT)
                return redirect('confirm_registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registrationForm
        })

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registation-successful.html', {
        'organizer_email': meetup.organizer_email
    })
