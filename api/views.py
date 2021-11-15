from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Prestamo
from.serializers import PrestamoSerializer

@api_view(['GET','POST'])
def prestamos(request):
    if request.method=='GET':
        listaprestamos=Prestamo.objects.all()
        setCursos=PrestamoSerializer(listaprestamos,many=True)
    elif request.method=='POST':
        serPrestamo=PrestamoSerializer(data=request.data)
        if serPrestamo.is_valid():
            serPrestamo.save()
            return Response(serPrestamo.data)
        else:
            return Response(serPrestamo.errors)
    return Response(setCursos.data)

@api_view(['GET','PUT','DELETE'])
def prestamodetalle(request,prestamo_id):
    objprestamo=Prestamo.objects.get(id=prestamo_id)
    if request.method=='GET':
        serPrestamo=PrestamoSerializer(objprestamo)
        return Response(serPrestamo.data)
    elif request.method=='PUT':
        serPrestamo=PrestamoSerializer(objprestamo,data=request.data)
        if serPrestamo.is_valid():
            serPrestamo.save()
            return Response(serPrestamo.data)
        else:
            return Response(serPrestamo.errors)
    elif request.method=='DELETE':
        objprestamo.delete()
        return Response(status=404)

