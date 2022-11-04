from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('restapidatapatient/',views.getdata,name="getdata"),
    path('restapionepatient/<int:id>',views.modify,name="modify"),
    path('restapidatadoctor/',views.getdatadoctor,name="getdata"),
    path('restapionedoctor/<int:id>',views.modifydoctor,name="modify")

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)