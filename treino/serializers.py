from rest_framework import serializers
from .models import (
    FichaUsuario,
    GrupoMuscular,
    EquipamentoAcademia,
    Exercicios,
    DivisaoTreino,
    Exercicio,
    TreinoPronto,
    TreinoCustom,
)


# Serializer for FichaUsuario Model
class FichaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaUsuario
        fields = ['id', 'nome', 'altura', 'peso', 'imc', 'data_nascimento', 'sexo']


# Serializer for GrupoMuscular Model
class GrupoMuscularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoMuscular
        fields = ['id', 'grupo_muscular']


# Serializer for EquipamentoAcademia Model
class EquipamentoAcademiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipamentoAcademia
        fields = [
            'id', 'maquina', 'tipo_peso', 'variacao_peso', 'equipamento_auxiliar'
        ]


# Serializer for Exercicios Model
class ExerciciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicios
        fields = [
            'id', 'peitoral', 'costas', 'ombros', 'biceps', 'triceps',
            'pernas', 'abdomen', 'outros', 'grupo_muscular'
        ]


# Serializer for DivisaoTreino Model
class DivisaoTreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisaoTreino
        fields = ['id', 'divisao']


# Serializer for Exercicio Model
class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = [
            'id', 'exercicio', 'equipamento', 'grupo_muscular', 'series',
            'repeticoes', 'peso', 'descanso'
        ]


# Serializer for TreinoPronto Model
class TreinoProntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreinoPronto
        fields = [
            'id', 'divisao_treino', 'aluno', 'exercicio',
            'frequencia_semanal'
        ]


# Serializer for TreinoCustom Model
class TreinoCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreinoCustom
        fields = ['id', 'frequencia_semanal', 'aluno', 'exercicio']
