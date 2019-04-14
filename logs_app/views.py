#render function pulls from 'templates' folder in directory
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

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
    return render(request, 'topic.html', context)

def new_topic(request):
    """Allow the user to create a new topic"""
    if request.method != 'POST':
        # It's a GET-no data submitted
        form = TopicForm()
        context = {'form': form}
        return render(request, 'new_topic.html', context)
    else:
        #It's a POST-send data to database
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs_app:topics'))

def new_entry(request, topic_name):
    """Create a new entry in a topic"""
    
    topic = Topic.objects.get(text=topic_name)
    
    if request.method != 'POST':
        #Return blank form
        form = EntryForm()
        context = {'topic': topic, 'form': form}
        return render(request, 'new_entry.html', context)
    else:
        #Send to database
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic

            new_entry.save()

            return HttpResponseRedirect(reverse('logs_app:topic', args=[topic_name]))

def edit_entry(request, topic_name, entry_id):
    """Load current content of an entry and allow it to be changed"""
    pass