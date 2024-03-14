from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializers,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers


# company/companyid/employees
@action(detail=True, methods=['get'])
def employees(self, request, pk=None):
    try:
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company)
        emp_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
        return Response(emp_serializer.data)
    except Exception as e:
        return Response({
            'message':'Company might not exist 404 error'
        })



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
