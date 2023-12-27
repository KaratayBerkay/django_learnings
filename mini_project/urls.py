"""
URL configuration for mini_project project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from user_service.views import UserViewGet, UserViewPost, UserViewPut, UserViewDelete, UserViewList
from user_service.views import JobView

router = DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    *router.urls,
    path("admin/", admin.site.urls),
    # path('swagger/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("user/get/<str:uuid_ref>/", UserViewGet.as_view(), name='user get'),
    path("user/add", UserViewPost.as_view(), name='user set'),
    path("user/list", UserViewList.as_view(), name='user list'),
    path("user/edit/<str:uuid_ref>/", UserViewPut.as_view(), name='user edit'),
    path("user/delete/<str:uuid_ref>/", UserViewDelete.as_view(), name='user delete'),
    path("job/", JobView.as_view()),
    path(
        "api/v1/",
        include(
            [
                path(
                    "swagger/",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="schema-swagger-ui",
                ),
                path(
                    "redoc/",
                    schema_view.with_ui("redoc", cache_timeout=0),
                    name="schema-redoc",
                ),
            ]
        ),
    ),
]
