import random

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import re

def phone_validators(value):
    reg = r"^(1[3|4|5|6|7|8|9])\d{9}$"
    if not re.match(reg, value):
        raise ValidationError('手机号错误')

class MessageSerializer(serializers.Serializer):
    phone = serializers.CharField(label="手机号",validators=[phone_validators, ])

class LoginView(APIView):

    def post(self,request,*args,**kwargs):
        print(request.data)
        return Response({"status":True})

class MessageView(APIView):

    def get(self,request,*args,**kwargs):
        # phone = request.query_params.get('phone')
        # print(phone)
        ser = MessageSerializer(data=request.query_params)
        if not ser.is_valid():
            return Response({"status": False,'message':"手机格式错误"})
        phone = ser.validated_data.get('phone')
        print(phone)
        import random
        rand_code = random.randint(1000,9999)

        return Response({"status": True})