from django import forms
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


class FichaUsuarioForm(forms.ModelForm):
    class Meta:
        model = FichaUsuario
        fields = ['nome', 'altura', 'peso', 'data_nascimento', 'sexo']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(choices=[
                ('F', 'Feminino'),
                ('M', 'Masculino'),
            ])
        }


class GrupoMuscularForm(forms.ModelForm):
    class Meta:
        model = GrupoMuscular
        fields = ['grupo_muscular']
        widgets = {
            'grupo_muscular': forms.Select(choices=GrupoMuscular.GRUPOS_MUSCULARES_CHOICES),
        }


class EquipamentoAcademiaForm(forms.ModelForm):
    class Meta:
        model = EquipamentoAcademia
        fields = ['maquina', 'tipo_peso', 'variacao_peso', 'equipamento_auxiliar']
        widgets = {
            'maquina': forms.Select(choices=EquipamentoAcademia.MAQUINAS_CHOICES),
            'tipo_peso': forms.Select(choices=EquipamentoAcademia.TIPOS_PESOS_CHOICES),
            'variacao_peso': forms.Select(choices=EquipamentoAcademia.VARIACOES_PESOS_CHOICES),
            'equipamento_auxiliar': forms.Select(choices=EquipamentoAcademia.EQUIPAMENTOS_AUXILIARES_CHOICES),
        }


class ExerciciosForm(forms.ModelForm):
    class Meta:
        model = Exercicios
        fields = [
            'peitoral', 'costas', 'ombros', 'biceps', 'triceps', 'pernas', 'abdomen', 'outros', 'grupo_muscular'
        ]
        widgets = {
            'peitoral': forms.Select(choices=Exercicios.PEITORAL_CHOICES),
            'costas': forms.Select(choices=Exercicios.COSTAS_CHOICES),
            'ombros': forms.Select(choices=Exercicios.OMBROS_CHOICES),
            'biceps': forms.Select(choices=Exercicios.BICEPS_CHOICES),
            'triceps': forms.Select(choices=Exercicios.TRICEPS_CHOICES),
            'pernas': forms.Select(choices=Exercicios.PERNAS_CHOICES),
            'abdomen': forms.Select(choices=Exercicios.ABDOMEN_CHOICES),
            'outros': forms.Select(choices=Exercicios.OUTROS_CHOICES),
        }


class DivisaoTreinoForm(forms.ModelForm):
    class Meta:
        model = DivisaoTreino
        fields = ['divisao']
        widgets = {
            'divisao': forms.Select(choices=DivisaoTreino.DIVISAO_CHOICES),
        }


class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['exercicio', 'equipamento', 'grupo_muscular', 'series', 'repeticoes', 'peso', 'descanso']
        widgets = {
            'descanso': forms.NumberInput(attrs={'placeholder': 'Descanso em segundos'}),
            'peso': forms.NumberInput(attrs={'placeholder': 'Peso em kg'}),
        }


class TreinoProntoForm(forms.ModelForm):
    class Meta:
        model = TreinoPronto
        fields = ['divisao_treino', 'aluno', 'exercicio', 'frequencia_semanal']


class TreinoCustomForm(forms.ModelForm):
    class Meta:
        model = TreinoCustom
        fields = ['aluno', 'exercicio', 'frequencia_semanal']
