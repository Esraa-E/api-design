from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('boards',views.BoardViewSet,basename='boards')
urlpatterns = [
    # path('',views.BoardUpdateView.as_view(),name='home'),
    # path('boards/<int:board_id>/',views.BoardTopics.as_view(),name='board_topics'),
    # path('boards_detail/<int:id>/',views.BoardDetail.as_view(),name='board_deatils'),
]
urlpatterns= urlpatterns + router.urls