#define URL route for index() view
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router=DefaultRouter()
router.register(r'Booking', views.BookingViewSet)

urlpatterns = [
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('', include(router.urls)),  
    path('api-token-auth/', obtain_auth_token)  
]