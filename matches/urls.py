from django.conf.urls import url, include
from .views import match_instance, add_or_edit_a_match,update_availability_status, save_a_generated_team, rate_performance_page, add_ratings_to_db, email_availability_reminder

urlpatterns = [
    url(r'^match_instance/(?P<groupid>\d+)/(?P<matchid>\d+)$', match_instance, name="matches"),
    url(r'^add_or_edit_a_match/(?P<groupid>\d+)/(?P<matchid>\d+)$', add_or_edit_a_match, name="add-edit-match"),
    url(r'^update_availability_status/(?P<matchid>\d+)/(?P<availability_table_id>\d+)$', update_availability_status, name="update-status"),
    url(r'^save_a_generated_team/(?P<groupid>\d+)/(?P<matchid>\d+)$', save_a_generated_team, name="save-team"),
    url(r'^rate_performance_page/(?P<matchid>\d+)$', rate_performance_page, name="rate-performance"),
    url(r'^add_ratings_to_db/(?P<matchid>\d+)$', add_ratings_to_db, name="submit-performance-ratings"),
    url(r'^email_availability_reminder/(?P<matchid>\d+)$', email_availability_reminder, name="email-availability-reminder"),
]