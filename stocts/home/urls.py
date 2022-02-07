from django.urls import path
from .views import *

#
urlpatterns = [
   path('', home, name = 'homepage'),
   path('age-calculator/', ageCalculator, name = 'agepage'),
   path('about/', about, name = 'about'),
   path('resume/', resume, name = 'resume'),
   path('contact', hom, name = 'homepag'),
   path('service/', service, name = 'service'),
   path('contact/', contact, name = 'contact'),
   path('add/', add, name = 'add'),
   path('predict_text/', predict_text, name = 'predict'),
   path('forms/', form_view, name = 'FormView'),
]
