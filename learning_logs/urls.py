"""Define URL patterns for learning logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'  # Required when using namespaces

urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),

    #show all topics.
    path('topcis/', views.topics, name='topics'),

    #Detailed page for the single topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Page for adding a new page
    path('new_topic/', views.new_topic, name = 'new_topic'),

    #Page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),

    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
    ]


    
    