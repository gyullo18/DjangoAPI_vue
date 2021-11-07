from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


class ApiView(View):
    @csrf_exempt
    def get(self, request):
        with open('./media/jsondatas/00279.json') as f:
            data = json.load(f)
        return JsonResponse(data)

    @csrf_exempt
    def post(self, request):
        return HttpResponse("Post 요청을 잘받았다")

    @csrf_exempt
    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")

    @csrf_exempt
    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")
