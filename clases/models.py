from django.db import models

class Usuario(models.Model):
    ROL_CHOICES = [
        ('Estudiante','Estudiante'),
        ('Profesor','Profesor'),
    ]

    Nombre = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Rol = models.CharField(max_length=10, choices=ROL_CHOICES)
    Autenticacion = models.TextField()

    def __str__(self):
        return self.Nombre

class Curso(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null= True, blank=True)
    Profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Estudiantes = models.ManyToManyField(Usuario, related_name='cursos', through='UsuarioCurso')

    def __str__(self):
        return self.Nombre

class UsuarioCurso(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Usuario', 'Curso')

    def __str__(self):
        return f"{self.Usuario} - {self.Curso}"

class Clase(models.Model):
    Fecha = models.DateField()
    Hora_Inicio = models.TimeField()
    Hora_Fin = models.TimeField()
    Aula = models.CharField(max_length=50, null=True, blank=True)
    Notas = models.TextField(null=True, blank=True)
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Clase de {self.Curso} el {self.Fecha}"
    
class Evaluacion(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True, blank=True)
    Fecha = models.DateField()
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre
    
class Tarea(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True, blank=True)
    Fecha_limite = models.DateField()
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Notificacion(models.Model):
    Titulo = models.CharField(max_length=100)
    Mensaje = models.TextField()
    Fecha_envio = models.DateTimeField(auto_now_add=True)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    Clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True, blank=True)
    Evaluacion = models.ForeignKey(Evaluacion, on_delete=models.SET_NULL, null=True, blank=True)
    Tarea = models.ForeignKey(Tarea, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Titulo