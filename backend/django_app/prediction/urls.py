from django.urls import path
import views as views

urlpatterns = [
    path('predict/', views.Ranger_Rank_Model_Predict.as_view(), name = 'api_predict'),
]
