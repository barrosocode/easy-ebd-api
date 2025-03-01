from rest_framework import serializers
from easy_ebd_app import models

# Gender Serializer
class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = '__all__'

# Person Serializer
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'

# Role Serializer
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'

# Turma Serializer
class TurmasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Turma
        fields = '__all__'

# Material Serializer
class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'

# Participant Serializer
class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Participant
        fields = '__all__'

# Aula Serializer
class AulasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aula
        fields = '__all__'

# Attendance Serializer
class AttendancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'

# Participant_Attendance Serializer
class Participant_AttendancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Participant_Attendance
        fields = '__all__'
