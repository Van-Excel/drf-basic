from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Snippets
from .serializers import SnippetSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status



# Create your views here.

# listing all existing snippets or creating a new snippet
@csrf_exempt
def snippet_list(request):

    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe= False)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
# listing an instance of a snippet or updating and deleting an instance of a snippet
def snippet_detail(request, pk):
    try:
        snippet = get_object_or_404(Snippets, pk = pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED, safe=False)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_404_NOT_FOUND, safe= False)

    elif request.method == "DELETE":
        snippet.delete()
        return JsonResponse(status = status.HTTP_204_NO_CONTENT, safe= False)
    
        