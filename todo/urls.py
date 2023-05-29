from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),
    path('homework/', include('homework.urls')),
    path('converter/', include('converter.urls'))
]
