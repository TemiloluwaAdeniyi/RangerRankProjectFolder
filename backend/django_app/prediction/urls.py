from django.urls import path
import prediction.views as views
 pip i
urlpatterns = [
    path('predict/', views.Ranger_Rank_Model_Predict.as_view(), name = 'api_predict'),
]