from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from core.models import Dare
# Create your views here.


class QRDareView(APIView):
    permission_classes = []
    renderer_classes = (TemplateHTMLRenderer, )
    def get(self, request, token):
        try:
            dare = Dare.objects.get(token=token)
            dare.count += 1
            dare.save()
        except Dare.DoesNotExist:
            Dare.objects.create(token=token, count=1)

        return Response(status=HTTP_200_OK, data={"message" : "done!"}, template_name='core/dare.html')

