from django.shortcuts import render,redirect,get_object_or_404
from .models import Smartphone
# Create your views here.
def smartphone(request):
    smartphones = Smartphone.objects.all()
    return render(request,'smartphone.html',context={'smartphones':smartphones})

def smartphone_det(request,pk):
    smartphone =Smartphone.objects.get(id=pk)
    return render(request,'smartphone_det.html',context={'smartphone':smartphone})


def create_smartphone(request):
    if request.method == 'POST':
        smartphone = Smartphone()
        smartphone.make = request.POST.get('make','')
        smartphone.model = request.POST.get('model','')
        smartphone.memory = request.POST.get('memory','')
        smartphone.color = request.POST.get('color','')
        smartphone.price = request.POST.get('price','')
        smartphone.description = request.POST.get('description','')
        smartphone.image = request.FILES.get('image','')
        
        smartphone.save()
        
        return redirect('smartphone_list')
    
    return render(request,'smartphone_create.html',{'smartphone':'smartphone'})



def update_smartphone(request,pk):
    smartphone = Smartphone.objects.get(id=pk)
    if request.method == 'POST':
        smartphone.make = request.POST.get('make',smartphone.make)
        smartphone.model = request.POST.get('model',smartphone.model)
        smartphone.memory = request.POST.get('memory',smartphone.memory)
        smartphone.color = request.POST.get('color',smartphone.color)
        smartphone.price = request.POST.get('price',smartphone.price)
        smartphone.description = request.POST.get('description',smartphone.description)
        smartphone.image = request.FILES.get('image',smartphone.image)
        smartphone.save()
        
        return redirect('smartphone_det', pk=pk)
    
    return render(request, 'smartphone_update.html', {'smartphone': smartphone})
        
    
def delete_smartphone(request,pk):
    smartphone = get_object_or_404(Smartphone,id=pk)
    if request.method =='POST':
        smartphone.delete()
        return redirect('smartphone_list')
    return render(request,'smartphone_delete.html',{'smartphone':smartphone})
    
    
    