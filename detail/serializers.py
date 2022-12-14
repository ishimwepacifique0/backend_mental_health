from rest_framework import serializers
from .models import *


class Detailapi(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['fullname','country','email','password']

class Detaildoctor(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','fullname','country','email','password','speciality','upload_image']