from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from app01.models import Area


def show_page(request,page_num=1):
    areas = Area.objects.filter(parent_id=1)
    paginator = Paginator(areas,10)
    page = paginator.page(page_num)
    datas = {
        'page':page
    }


    return render(request,'show_page.html',datas)