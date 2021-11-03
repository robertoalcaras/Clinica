from datetime import datetime
from django.db import models
from paciente.models import Paciente
from ComunicOral.models import ComunicOral

class AvaliacaoAD(models.Model):
    ORELHA_CHOICE = (
        ('OE', 'Orelha Esquerda'),
        ('OD', 'Orelha Direita'),
        ('AM', 'Ambas'),
    )
    DataAvaliacao = models.DateTimeField(default=datetime.now)
    QOrelha = models.CharField(max_length=2, choices=ORELHA_CHOICE)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
      
    class Meta:
        verbose_name_plural = "Avaliação Adulto"
    
    def __str__(self):
        return str(self.paciente)
    

class ComunicOralidade(models.Model):
    avaliacaoAD = models.ForeignKey(AvaliacaoAD, on_delete=models.DO_NOTHING)
    ComunicOral = models.ForeignKey(ComunicOral, on_delete=models.DO_NOTHING)
    resp_oralidade = models.CharField(
        default="N",
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Nâo'),
        )
    )
    
    class Meta:
        verbose_name_plural = "Respostas das Perguntas"    
        
    def __str__(self):
        return str(self.resp_oralidade)    
        