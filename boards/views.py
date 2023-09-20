from django.forms.models import BaseModelForm
from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from django.views.generic import UpdateView
from django.utils import timezone

# Create your views here.
# class BroadList(generics.ListCreateAPIView):
#     queryset=Board.objects.all()
#     serializer_class =BoardSerializer

# class BoardUpdateView(UpdateView):
#     model=Board
#     fields=('name','description',)
#     template_name='soso.html'
#     pk_url_kwarg='Board_id'
#     context_object_name='Board'
    
#     def form_valid(self,form):
#         Board=form.save(commit=False)
#         Board.save()
#         return redirect('')
        

class BoardViewSet(viewsets.ModelViewSet):
    queryset= Board.objects.all()
    serializer_class=BoardSerializer

# class BoardTopics(generics.ListCreateAPIView):
#     queryset=Topic.objects.all()
#     serializer_class=TopicSerializer
#     lookup_field='Board_id'

# class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Board.objects.all()
#     serializer_class =BoardSerializer
#     lookup_field='id'




# 
# def board_topics(request,board_id):
#     board=get_object_or_404(Board,pk=board_id)
#     data={
#         "results":{
#             "name":board.name,
#             "description": board.description,
#         }
#     }
#     return JsonResponse(data)