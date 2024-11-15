from django.db import models
from django.contrib.auth.models import User


class Loja(models.Model):#tabela loja com os campos codigo e nome
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Servico(models.Model):#tabela servico com os campos codigo, nome, preco_min e preco_max
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    preco_min = models.DecimalField(max_digits=10, decimal_places=2)
    preco_max = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo


class EmissaoOrdemServico(models.Model):#tabela emissao_ordem_servico com os campos nome, numero_os, empresa, servico, produto, data e usuario
    numero_os = models.CharField(max_length=20)
    empresa = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True) 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.nome
    
class OrdemServico(models.Model):
    numero_os = models.CharField(max_length=20, primary_key=True, unique=True)  # Número da OS como chave primária
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"OS {self.numero_os} - {self.loja} - {self.servico}"