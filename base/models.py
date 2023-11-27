from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):

    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE, # Si el usuario es borrado, sus tareas pendientes tambien se borrarán
                                null = True, # Elvalor de usuario puede estar vacìo
                                blank = True, # El registro puede estar en blanco.
                                )
    
    titulo = models.CharField(max_length = 200)

    descripcion = models.TextField(null = True,
                                   blank = True)
    
    completo = models.BooleanField(default = False) # Por defecto que aparezca no completa

    creado = models.DateTimeField(auto_now_add = True) # Se genera automaticamente la fecha y hora de creaciòn.

    def __str__(self):
        return self.titulo
    
    class Meta: 
        ordering = ['completo'] # Como se van a ordenar las tareas dentro de nuestra tabla, campo llamado: completo determinará el orden