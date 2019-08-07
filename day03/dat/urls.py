from django.conf.urls import url

from dat import views

urlpatterns = [
    url(r'^add/$',views.add,name='add'),
    url(r'^modify/$',views.modify,name='modify'),
    url(r'^delete/$',views.delete,name='delete'),

    # 查询
    url(r'^find/$',views.find,name='find'),
    url(r'^paremeter/$',views.paremeter,name='paremeter'),

]