from django.urls import path

from pages.views import AboutPageView, HomePageView

urlpatterns = [
    path("pages/", HomePageView.as_view(), name="pages_home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
