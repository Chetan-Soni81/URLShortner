from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.template import loader
import uuid
from .models import Links 

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Links(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Links.objects.get(uuid=pk)
    if 'https://' in url_details.link:
        return redirect(url_details.link)
    else:
        return redirect('https://' + url_details.link)
