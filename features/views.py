from django.views.generic import ListView, DetailView
from .models import *

class FeaturesListView(ListView):
    model = Features
    template_name = 'features/features_list.html'
    context_object_name = 'features_list'

class FeatureDetailsView(DetailView):
    model = Features
    template_name = 'features/feature_details.html'
    context_object_name = 'feature_details'