from django.conf.urls import patterns, url
from .views import (ProfileView, GrantRequestListView, MembershipView,
                    MembershipApplyView)

urlpatterns = patterns(
    '',
    url(r'^$', ProfileView.as_view(), name='profile_home'),

    url(r'^grants/$', GrantRequestListView.as_view(),
        name='profile_grantreq_list'),

    url(r'^membership/$', MembershipView.as_view(), name='profile_membership'),
    url(r'^membership/apply/$', MembershipApplyView.as_view(), name='profile_membership_apply'),
)
