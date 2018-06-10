# @Time    : 18-6-5 下午2:19
# @Author  : wengwenyu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import index,list_1,base,show

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^list/$',list_1,name='list'),
    url(r'^base/$',base,name='base'),
    url(r'^tags/(?P<tid>[0-9]+)$',list_1,name='tags'),
    url(r'^detail/(?P<did>[0-9]+)$',show,name='detail'),

]
