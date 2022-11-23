from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeaturesListView.as_view(), name='features_list'),
    path('detail/<int:pk>', views.FeatureDetailsView.as_view(), name='feature_details'),
]