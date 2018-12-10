from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    # always use include() except for this ⤵️
    path('admin/', admin.site.urls),
]