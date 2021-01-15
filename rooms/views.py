from django.shortcuts import render
from django.core.paginator import Paginator  # 장고가 도와주는
from . import models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)  # 오브젝트 목록, 한페이지당 나오는 오브젝트 개수
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"page", rooms})
