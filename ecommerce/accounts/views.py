from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class Registerview(APIView):
    
    def post(self,request):
        username = request.data[username]
        password = request.data[password]
        user = user(username=username)
        user.set_password(password)
        refresh =RefreshToken.for_user(user)
        
        return Response(      
"status":"success"  ,
'refresh':str(refresh) , 'access': strrefresh.access_token)
