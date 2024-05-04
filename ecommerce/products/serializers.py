from rest_framework import serializers
from.models import *


class ProductSerializers(serializers.ModelSerializer):
    class meta:
        model = Product
        field = '__all__'