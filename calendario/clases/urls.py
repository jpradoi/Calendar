from django.urls import path
from .views import UsuarioList, UsuarioDetail, CursoList, CursoDetail, EvaluacionList, EvaluacionDetail, ClaseList, ClaseDetail, TareaList, TareaDetail, NotificacionList, NotificacionDetail

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),
    path('cursos/', CursoList.as_view(), name='curso-list'),
    path('cursos/<int:pk>/', CursoDetail.as_view(), name='curso-detail'),
    path('evaluaciones/', EvaluacionList.as_view(), name='evaluacion-list'),
    path('evaluaciones/<int:pk>/', EvaluacionDetail.as_view(), name='evaluacion-detail'),
    path('clases/', ClaseList.as_view(), name='clase-list'),
    path('clases/<int:pk>/', ClaseDetail.as_view(), name='clase-detail'),
    path('tareas/', TareaList.as_view(), name='tarea-list'),
    path('tareas/<int:pk>/', TareaDetail.as_view(), name='tarea-detail'),
    path('notificaciones/', NotificacionList.as_view(), name='notificacion-list'),
    path('notificaciones/<int:pk>/', NotificacionDetail.as_view(), name='notificacion-detail'),
]
