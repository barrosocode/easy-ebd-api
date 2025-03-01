from rest_framework import viewsets
from easy_ebd_app.api import serializers
from easy_ebd_app import models

# Gender ViewSet
class GenderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GendersSerializer
    queryset = models.Gender.objects.all()

# Person ViewSet
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PeopleSerializer
    queryset = models.Person.objects.all()

# Role ViewSet
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RolesSerializer
    queryset = models.Role.objects.all()

# Turma ViewSet
class TurmaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TurmasSerializer
    queryset = models.Turma.objects.all()

# Material ViewSet
class MaterialViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MaterialsSerializer
    queryset = models.Material.objects.all()

# Participant ViewSet
class ParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ParticipantsSerializer
    queryset = models.Participant.objects.all()

# Aula ViewSet
class AulaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AulasSerializer
    queryset = models.Aula.objects.all()

# Attendance ViewSet
class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AttendancesSerializer
    queryset = models.Attendance.objects.all()

# Participant_Attendance ViewSet
class Participant_AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Participant_AttendancesSerializer
    queryset = models.Participant_Attendance.objects.all()
