from django.core.serializers import serialize
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# from .models import labeling

# 주석 코드 - 모델 + 시리얼라이저 완성 후 풀어볼 예정 : 폭풍 에러뜨는중 ㅠ

class ApiView(APIView):
    @csrf_exempt
    def get(self, request):
        with open('./media/labelingdatas/00279.json') as f:
            data = json.load(f)
        return JsonResponse(data)
        # label = labeling.objects.all()
        # data = json.loads(serialize('json', label))
        # return JsonResponse({'items': data})

    @csrf_exempt
    def post(self, request):
        return HttpResponse("Post 요청을 잘받았다")
        # if request.META['CONTENT_TYPE'] == "application/json":
        #     request = json.loads(request.body)
        # label = labeling(version=request['version'],
        #                  shape=request['shape'],
        #                  imagePath=request['imagePath'],
        #                  imageHeight=request['imageHeight'])
        #                  imageWidth=request['imageWidth'])
        # else:
        # label = labeling(version=request.POST['version'],
        #             #    hape=request.POST['shape'],
        #             #    imagePath=request.POST['imagePath'],
        #             #    imageHeight=request.POST['imageHeight'])
        #             #    imageWidth=request.POST['imageWidth'])
        #
        # label.save()
        # return HttpResponse(status=200)


    @csrf_exempt
    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")
        # request = json.loads(request.body)
        # group_id = request['group_id']
        # shape_type = request['shape_type']
        # label = get_object_or_404(labeling, pk=group_id)
        # label.save()
        # return HttpResponse(status=200)

    @csrf_exempt
    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")
        # request = json.loads(request.body)
        # group_id = request['group_id']
        # label = get_object_or_404(labeling, pk=group_id)
        # label.delete()
        # return HttpResponse(status=200)
