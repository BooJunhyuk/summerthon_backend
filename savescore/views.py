from django.shortcuts import render,get_object_or_404
from .models import Score
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,CreateAPIView

from rest_framework.views import APIView
from .serializers import ScoreSerializer


class CreateScore(CreateAPIView):#post임
        #queryset=Score.objects.all() #create이기 때문에 쿼리셋 쓸 필요 없음
        serializer_class=ScoreSerializer

class UpdateScore456(APIView):
    serializer_class = ScoreSerializer

    def get_object(self, pk):
        score = Score.objects.get(pk=pk)
        return score

    def post(self, request, pk):
        score = self.get_object(pk)
        score.score4 = request.data.get('score4', score.score4)
        score.score5 = request.data.get('score5', score.score5)
        score.score6 = request.data.get('score6', score.score6)
        score.save()
        serializer = ScoreSerializer(score)
        return Response(serializer.data)
    
class UpdateScore78910(APIView):
    serializer_class = ScoreSerializer

    def get_object(self, pk):
        score = Score.objects.get(pk=pk)
        return score

    def post(self, request, pk):
        score = self.get_object(pk)
        score.score7 = request.data.get('score7', score.score7)
        score.score8 = request.data.get('score8', score.score8)
        score.score9 = request.data.get('score9', score.score9)
        score.score10 = request.data.get('score10', score.score10)
        score.save()
        serializer = ScoreSerializer(score)
        return Response(serializer.data)
    

class GetScore(RetrieveAPIView):#RetriveAPIView는 pk값이 필요함 //GET임
    queryset=Score.objects.all()
    serializer_class=ScoreSerializer
    
    