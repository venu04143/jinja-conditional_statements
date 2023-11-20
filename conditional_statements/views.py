from django.shortcuts import render

# Create your views here.
def statements(request):
    dict={'a':50,'b':60,'c':40}
    return render(request,'conditions.html',context=dict)