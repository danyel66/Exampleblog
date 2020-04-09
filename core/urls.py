from django.urls import path
from .views import post_list, post_detail, post_share, post_search
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import PostSitemap
from core.feeds import LatestPostsFeed


app_name = 'core'

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', post_list, name='post_list'),
    # path('', PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail,
         name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', post_search, name='post_search'),
]
