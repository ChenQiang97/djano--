from django.conf.urls import url
from user import views
from user.views import RegisterView,ActiveView,LoginView,UserInfoView,UserOrderView,AddressView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^register$',views.register,name='register'),#注册
    # url(r'^register_handle$',views.register_handle,name='register_handle'),#注册处理

    url(r'^register',RegisterView.as_view(),name='register'),#注册(类视图方法)
    url(r'^active/(?P<token>.*)$',ActiveView.as_view(),name='active'),#用户激活
    url(r'^login$',LoginView.as_view(),name='login'),#登录
    url(r'^logout$',LogoutView.as_view(),name='logout'), #注销登录

    # # 登录检测,未登录的话跳转到 setting.LOGIN_URL 并将当前访问的绝对路径船底到查询字符串
    # # 如: /accounts/login/?next=/polls/3/
    # url(r'^$', login_required(UserInfoView.as_view()), name='user'), # 用户中心-信息页
    # url(r'^order$', login_required(UserOrderView.as_view()), name='order'), # 用户中心-订单页
    # url(r'^address$', login_required(AddressView.as_view()), name='address'), # 用户中心-地址页

    # 登录检测,未登录的话跳转到 setting.LOGIN_URL 并将当前访问的绝对路径船底到查询字符串
    # 如: /accounts/login/?next=/polls/3/
    # 使用 until.mixin
    url(r'^$', UserInfoView.as_view(), name='user'), # 用户中心-信息页
    url(r'^order$',UserOrderView.as_view(), name='order'), # 用户中心-订单页
    url(r'^address$',AddressView.as_view(), name='address'), # 用户中心-地址页
]
