from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_data

class GetData(TemplateView):
    template_name = 'ricky_morty.html'
    def get_context_data(self, *args, **kwargs):
           
        context = {
            'data' : get_data()
        }
        return context
