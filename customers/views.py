from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
from .models import Customer
from .serializers import CustomerSerializer


@api_view(['POST'])
def customer_create(request):
    print(f'create but method is {request.method}')
    print(f'get = {request.GET}')
    print(f'post = {request.POST}')
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def customers_list(request):
    """
 List  customers, or create a new customer.
 """
    print(request.method)
    print(request.data)
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, context={'request': request}, many=True)
        print('get')
        return Response({'data': serializer.data, 'count': 1, 'numpages': 1,
                         'nextlink': '/api/customers/?page=' + str(nextPage),
                         'prevlink': '/api/customers/?page=' + str(previousPage)})



@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        customer = Customer.objects.get(pk=pk)
        print(customer)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
