#render function pulls from 'templates' folder in directory
from django.shortcuts import render

from logs_app.models import Topic

# Create your views here.
def index(request):
    """The home page for logs_app"""
    return render(request, 'index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def topic(request, topic_name):
    """Detail page for one topic"""
    topic = Topic.objects.get(text=topic_name)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topics.html', context)

