from django.db import models
from uuid import uuid4

# Gender
class Gender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=9, null=False, unique=True)

# Person
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=14, null=False, unique=True)
    birth = models.DateField(null=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    # email
    # password

# Role
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=15, null=False, unique=True)

# Turma
class Turma(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40, null=False, unique=True)
    description = models.TextField()

# Material
class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField(null=True)
    link = models.CharField(max_length=150, null=False)

# Participant
class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

# Aula
class Aula(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField()
    date = models.DateField(null=False)

# Attendance (lista de presença)
class Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)

# Participant_Attendance
class Participant_Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    oracao = models.BooleanField(null=False, default=False)
    leitura = models.BooleanField(null=False, default=False)
    licao = models.BooleanField(null=False, default=False)
    culto = models.BooleanField(null=False, default=False)
