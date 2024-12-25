from django.db import models


class FichaUsuario(models.Model):
    nome = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=2)
    def __str__(self):
        return self.nome

class GrupoMuscular(models.Model):
    GRUPOS_MUSCULARES_CHOICES = [
        ('peitoral', 'Peitoral'),
        ('costas', 'Costas'),
        ('ombros', 'Ombros'),
        ('biceps', 'Bíceps'),
        ('triceps', 'Tríceps'),
        ('pernas', 'Pernas'),
        ('abdomen', 'Abdômen'),
        ('panturrilhas', 'Panturrilhas'),
        ('gluteos', 'Glúteos'),
        ('antebracos', 'Antebraços'),
    ]

    grupo_muscular = models.CharField(
        max_length=50,
        choices=GRUPOS_MUSCULARES_CHOICES,
        unique=True,
        verbose_name="Grupo Muscular"
    )

    def __str__(self):
        return self.get_grupo_muscular_display()

class EquipamentoAcademia(models.Model):
    # Choices para Máquinas
    MAQUINAS_CHOICES = [
        ('smith', 'Máquina Smith'),
        ('crossover', 'Crossover'),
        ('pulley', 'Pulley'),
        ('leg_press', 'Leg Press'),
        ('extensora', 'Máquina Extensora'),
        ('flexora', 'Máquina Flexora'),
        ('hack_squat', 'Hack Squat'),
        ('supino', 'Máquina de Supino'),
        ('remada_sentada', 'Máquina de Remada Sentada'),
        ('peck_deck', 'Peck Deck'),
        ('cable_cross', 'Cable Cross'),
        ('remada_t_bar', 'Remada T-Bar'),
        ('extensor_de_panturrilha', 'Extensor de Panturrilha'),
        ('cadeira_adutora', 'Cadeira Adutora'),
        ('cadeira_abdutora', 'Cadeira Abdutora'),
    ]

    # Choices para Tipos de Pesos
    TIPOS_PESOS_CHOICES = [
        ('halteres', 'Halteres'),
        ('barras', 'Barras'),
        ('anilhas', 'Anilhas'),
        ('kettlebells', 'Kettlebells'),
        ('medicine_ball', 'Bola Medicinal'),
        ('caneleiras', 'Caneleiras'),
    ]

    # Choices para Variações de Pesos
    VARIACOES_PESOS_CHOICES = [
        ('fixos', 'Pesos Fixos'),
        ('ajustaveis', 'Pesos Ajustáveis'),
        ('livres', 'Pesos Livres'),
        ('acoplados', 'Pesos Acoplados'),
    ]

    # Choices para Equipamentos Auxiliares
    EQUIPAMENTOS_AUXILIARES_CHOICES = [
        ('corda', 'Corda de Pular'),
        ('roda_abdominal', 'Roda Abdominal'),
        ('step', 'Step'),
        ('prancha_abdominal', 'Prancha Abdominal'),
        ('bola_estabilidade', 'Bola de Estabilidade'),
        ('elásticos', 'Elásticos de Resistência'),
        ('battle_ropes', 'Battle Ropes'),
    ]

    # Campos do modelo
    maquina = models.CharField(max_length=50, choices=MAQUINAS_CHOICES, blank=True, null=True)
    tipo_peso = models.CharField(max_length=50, choices=TIPOS_PESOS_CHOICES, blank=True, null=True)
    variacao_peso = models.CharField(max_length=50, choices=VARIACOES_PESOS_CHOICES, blank=True, null=True)
    equipamento_auxiliar = models.CharField(max_length=50, choices=EQUIPAMENTOS_AUXILIARES_CHOICES, blank=True, null=True)

    def __str__(self):
        return (
            self.maquina or
            self.tipo_peso or
            self.variacao_peso or
            self.equipamento_auxiliar or
            "Equipamento Não Especificado"
        )


class Exercicios(models.Model):
    PEITORAL_CHOICES = [
        ('supino_reto', 'Supino Reto'),
        ('supino_inclinado', 'Supino Inclinado'),
        ('supino_declinado', 'Supino Declinado'),
        ('crucifixo_reto', 'Crucifixo Reto'),
        ('crucifixo_inclinado', 'Crucifixo Inclinado'),
        ('crucifixo_declinado', 'Crucifixo Declinado'),
        ('peck_deck', 'Peck Deck'),
        ('cross_over', 'Cross Over'),
        ('supino_halteres', 'Supino com Halteres'),
        ('pressao_peitoral', 'Pressão Peitoral'),
    ]
    COSTAS_CHOICES = [
        ('remada_curvada', 'Remada Curvada'),
        ('remada_unilateral', 'Remada Unilateral'),
        ('remada_cavalinho', 'Remada Cavalinho'),
        ('pulley_frontal', 'Pulley Frontal'),
        ('pulley_traseiro', 'Pulley Traseiro'),
        ('barra_fixa', 'Barra Fixa'),
        ('pulldown', 'Pulldown'),
        ('levantamento_terra', 'Levantamento Terra'),
        ('remada_invertida', 'Remada Invertida'),
        ('barbell_row', 'Barbell Row'),
        ('deadlift_romano', 'Deadlift Romano'),
    ]
    OMBROS_CHOICES = [
        ('desenvolvimento_reto', 'Desenvolvimento Reto'),
        ('desenvolvimento_halteres', 'Desenvolvimento com Halteres'),
        ('elevacao_lateral', 'Elevação Lateral'),
        ('elevacao_frontal', 'Elevação Frontal'),
        ('remada_alta', 'Remada Alta'),
        ('crucifixo_invertido', 'Crucifixo Invertido'),
        ('arnold_press', 'Arnold Press'),
        ('press_militar', 'Press Militar'),
        ('face_pulls', 'Face Pulls'),
        ('delt_reverse', 'Delt Reverse'),
    ]
    BICEPS_CHOICES = [
        ('rosca_direta', 'Rosca Direta'),
        ('rosca_martelo', 'Rosca Martelo'),
        ('rosca_invertida', 'Rosca Invertida'),
        ('rosca_concentrada', 'Rosca Concentrada'),
        ('rosca_scott', 'Rosca Scott'),
        ('rosca_barriga', 'Rosca Barriga'),
        ('curl_pulley', 'Curl no Pulley'),
        ('drag_curl', 'Drag Curl'),
    ]
    TRICEPS_CHOICES = [
        ('triceps_pulley', 'Tríceps no Pulley'),
        ('triceps_testa', 'Tríceps Testa'),
        ('mergulho_triceps', 'Mergulho no Banco'),
        ('triceps_coice', 'Tríceps Coice'),
        ('triceps_frances', 'Tríceps Francês'),
        ('skull_crusher', 'Skull Crusher'),
        ('triceps_diamante', 'Tríceps Diamante'),
        ('kickback_triceps', 'Kickback Tríceps'),
    ]
    PERNAS_CHOICES = [
        ('agachamento_livre', 'Agachamento Livre'),
        ('agachamento_smith', 'Agachamento no Smith'),
        ('leg_press', 'Leg Press'),
        ('extensora', 'Cadeira Extensora'),
        ('flexora', 'Cadeira Flexora'),
        ('afundos', 'Afundos'),
        ('panturrilha_sentada', 'Panturrilha Sentada'),
        ('panturrilha_em_pe', 'Panturrilha em Pé'),
        ('agachamento_bulgaro', 'Agachamento Búlgaro'),
        ('agachamento_femorais', 'Agachamento com Femorais'),
        ('hip_thrust', 'Hip Thrust'),
        ('passada', 'Passada'),
        ('sissy_squat', 'Sissy Squat'),
        ('leg_extension', 'Extensão de Perna'),
    ]
    ABDOMEN_CHOICES = [
        ('abdominal_crunch', 'Abdominal Crunch'),
        ('prancha_isometrica', 'Prancha Isométrica'),
        ('abdominal_inferior', 'Abdominal Inferior'),
        ('abdominal_obliquo', 'Abdominal Oblíquo'),
        ('elevação_pernas', 'Elevação de Pernas'),
        ('abdominal_bicycle', 'Abdominal Bicycle'),
        ('abdominal_em_rolamento', 'Abdominal em Rolo'),
        ('abdominal_terra', 'Abdominal Terra'),
        ('plank_rotacional', 'Plank Rotacional'),
        ('ab_wheel', 'Roda Abdominal'),
    ]
    OUTROS_CHOICES = [
        ('stiff', 'Stiff'),
        ('kettlebell_swing', 'Kettlebell Swing'),
        ('burpee', 'Burpee'),
        ('jump_squat', 'Jump Squat'),
        ('remada_sentada', 'Remada Sentada'),
        ('pull_over', 'Pull Over'),
        ('puxada_no_cabo', 'Puxada no Cabo'),
        ('clean_and_press', 'Clean and Press'),
        ('snatch', 'Snatch'),
        ('deadlift_sumô', 'Deadlift Sumô'),
        ('box_jump', 'Box Jump'),
        ('mountain_climber', 'Mountain Climber'),
        ('pistol_squat', 'Pistol Squat'),
        ('battle_ropes', 'Battle Ropes'),
    ]


    peitoral = models.CharField(max_length=50, choices=PEITORAL_CHOICES, blank=True, null=True)
    costas = models.CharField(max_length=50, choices=COSTAS_CHOICES, blank=True, null=True)
    ombros = models.CharField(max_length=50, choices=OMBROS_CHOICES, blank=True, null=True)
    biceps = models.CharField(max_length=50, choices=BICEPS_CHOICES, blank=True, null=True)
    triceps = models.CharField(max_length=50, choices=TRICEPS_CHOICES, blank=True, null=True)
    pernas = models.CharField(max_length=50, choices=PERNAS_CHOICES, blank=True, null=True)
    abdomen = models.CharField(max_length=50, choices=ABDOMEN_CHOICES, blank=True, null=True)
    outros = models.CharField(max_length=50, choices=OUTROS_CHOICES, blank=True, null=True)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.PROTECT, blank=True, null=True)


def __str__(self):
        return f"{self.peitoral or self.costas or self.ombros or self.biceps or self.triceps or self.pernas or self.abdomen or self.outros}"

class DivisaoTreino(models.Model):
    DIVISAO_CHOICES = [
        ('fullbody', 'Fullbody (Corpo Inteiro)'),
        ('ab', 'AB (Alternância de Dois Grupos)'),
        ('abc', 'ABC (Três Grupos)'),
        ('abcd', 'ABCD (Quatro Grupos)'),
        ('abcde', 'ABCDE (Cinco Grupos)'),
        ('push_pull_legs', 'Push/Pull/Legs (Empurrar/Puxar/Pernas)'),
        ('upper_lower', 'Upper/Lower (Parte Superior/Inferior)'),
        ('bodybuilding_split', 'Bodybuilding Split (Divisão de Musculação)'),
        ('calistenia', 'Calistenia'),
        ('hiit', 'HIIT (Treino Intervalado de Alta Intensidade)'),
    ]

    divisao = models.CharField(
        max_length=50,
        choices=DIVISAO_CHOICES,
        unique=True,
        verbose_name="Divisão de Treino",
    )

    def __str__(self):
        return self.get_nome_display()


class Exercicio(models.Model):
    exercicio = models.ForeignKey(Exercicios, on_delete=models.PROTECT)
    equipamento = models.ForeignKey(EquipamentoAcademia, on_delete=models.PROTECT)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.PROTECT)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    peso = models.IntegerField()
    descanso = models.IntegerField()

    def __str__(self):
        return {self.exercicio}


class TreinoPronto(models.Model):
    divisao_treino = models.ForeignKey(DivisaoTreino, on_delete=models.PROTECT)
    aluno = models.ForeignKey(FichaUsuario, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.PROTECT)
    frequencia_semanal = models.IntegerField()

    def __str__(self):
        return f'Treino pronto de {self.aluno.nome} - Treino: {self.divisao_treino}, {self.frequencia_semanal} vezes/semana'

class TreinoCustom(models.Model):
    frequencia_semanal = models.IntegerField()
    aluno = models.ForeignKey(FichaUsuario, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.PROTECT)


    def __str__(self):
        return f'Treino personalizado de {self.aluno.nome}'