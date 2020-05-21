from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .serializers import DetailSerializers
from .models import Details


@api_view(['GET', 'POST'])
def apiOverView(request):
    print("okk")
    return JsonResponse("API BASE POINT", safe=False)


@api_view(['GET'])
def detailsList(request):
    details = Details.objects.all()

    categary_id = request.query_params.get('CATEGORY_ID', '')
    categories = request.query_params.get('Categories', '')
    item_id = request.query_params.get('ITEM_ID', '')
    english_name = request.query_params.get('ENGLISH_NAME', '')
    price = request.query_params.get('PRICE', '')
    if categary_id:
        details_categary_id = details.filter(CATEGORY_ID=categary_id)
        print(details_categary_id)
        serializer = DetailSerializers(details_categary_id, many=True)
        return Response(serializer.data)

    if categories:
        details_categories = details.filter(Categories=categories)
        print(details_categories)
        serializer = DetailSerializers(details_categories, many=True)
        return Response(serializer.data)

    if item_id:
        details_item_id = details.filter(ITEM_ID=item_id)
        print(details_item_id)
        serializer = DetailSerializers(details_item_id, many=True)
        return Response(serializer.data)

    if english_name:
        details_english_name = details.filter(ENGLISH_NAME=english_name)
        print(details_english_name)
        serializer = DetailSerializers(details_english_name, many=True)
        return Response(serializer.data)

    if price:
        details_price = details.filter(PRICE=price)
        print(details_price)
        serializer = DetailSerializers(details_price, many=True)
        return Response(serializer.data)

    serializer = DetailSerializers(details, many=True)
    return Response(serializer.data)
