from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^log_out/$', views.log_out, name="log_out"),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^save_product/(?P<sub_id>[0-9]+)/$', views.save_product, name='save_product'),
    url(r'^list_saved_products/$', views.list_saved_products, name='list_saved_products'),
]