from rest_framework import serializers
from .models import Products, Options, Orders, QnAs, Comments, Carosel, MainCategory, SubCategory


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Options
        fields = "__all__"


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class QnASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QnAs
        fields = "__all__"


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class CaroselSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carosel
        fields = "__all__"

class MainCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainCategory
        fields = "__all__"

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
