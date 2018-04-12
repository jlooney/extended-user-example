from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User

class HomePageView(TemplateView):
    template_name = 'home.html'


class UserProfileView(View):
    def get(self, request, username):

        try:
            user = User.objects.get(username=username)
        except:
            user = None

        context = {
            "viewed_user": user
        }

        return render(request, "user_profile.html", context)