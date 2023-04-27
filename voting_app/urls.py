from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('host_event_page/', views.host_event_page, name='host_event_page'),
    path('participate_to_vote/', views.participate_to_vote, name='participate_to_vote'),
    path('event_page/<event_code>/', views.event_page, name='event_page'),
    path('view_event/<event_code>/', views.view_event, name='view_event'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage_events/', views.manage_events, name='manage_events'),
    path('edit_event/<event_id>', views.edit_event, name='edit_event'),
    path('unvote/<event_code>/<voted_for>', views.unvote, name='unvote'),
    path('delete_event/<event_id>', views.delete_event, name='delete'),
    path('create_campaign/', views.create_campaign, name='create_campaign'),
    path('stats/', views.stats, name='stats'),
]