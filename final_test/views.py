from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def custom_api(request):
    return Response({"mensaje": "API personalizada funcionando correctamente"})

