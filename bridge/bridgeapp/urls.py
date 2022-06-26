from django.urls import path
from .views import BridgeHomeView, BridgeCategoryView, BridgeThreadView, BridgeAuthenticateView, BridgeLogOutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # home page
    path('', login_required(BridgeHomeView.as_view()), name='home'),
    # single category page
    path('categories/<int:category_id>/<str:category_slug>', login_required(BridgeCategoryView.as_view()), name='category'),
    # single thread page
    path('threads/<int:thread_id>/<int:resp_id>', login_required(BridgeThreadView.as_view()), name='thread'),
    # login page
    path('login', BridgeAuthenticateView.as_view(), name='login'),
    path('logout', login_required(BridgeLogOutView.as_view()), name='logout'),
    # serve favicon from '/static'
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favison.ico'))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # add static assets
