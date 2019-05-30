from django.db import models

# Create your models here.
class Categoria (models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

    def __int__(self):
        return self.id

class Habilidade (models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

    def __int__(self):
        return self.id

class Tipo (models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

    def __int__(self):
        return self.id

class Fraqueza (models.Model):
    nome = models.ForeignKey('Tipo',on_delete=models.PROTECT)

    def __str__(self):
        return self.nome.nome

    def __int__(self):
        return self.id

class Evolucao (models.Model):
    nome = models.CharField(max_length=120)
    peso = models.FloatField(max_length=15)
    altura = models.FloatField(max_length=15)
    hp = models.PositiveIntegerField()
    ataque = models.PositiveIntegerField()
    defesa = models.PositiveIntegerField()
    ataque_especial = models.PositiveIntegerField()
    defesa_especial = models.PositiveIntegerField()
    fk_categoria = models.ForeignKey('Categoria',on_delete=models.PROTECT)
    fk_habilidade = models.ManyToManyField(Habilidade)
    fk_tipo = models.ManyToManyField(Tipo)
    fk_fraqueza = models.ManyToManyField(Fraqueza)
    imagem = models.FileField(upload_to='fotos/')

    def __str__(self):
        return self.nome

    def __int__(self):
        return self.id

class Pokemon (models.Model):
    nome = models.CharField(max_length=120)
    peso = models.FloatField(max_length=15)
    altura = models.FloatField(max_length=15)
    hp = models.PositiveIntegerField()
    ataque = models.PositiveIntegerField()
    defesa = models.PositiveIntegerField()
    ataque_especial = models.PositiveIntegerField()
    defesa_especial = models.PositiveIntegerField()
    fk_categoria = models.ForeignKey('Categoria',on_delete=models.PROTECT)
    fk_habilidade = models.ManyToManyField(Habilidade)
    fk_tipo = models.ManyToManyField(Tipo)
    fk_fraqueza = models.ManyToManyField(Fraqueza)
    fk_evolucao =models.ForeignKey('Evolucao',on_delete=models.PROTECT)
    imagem = models.FileField(upload_to='fotos/')

    def __str__(self):
        return self.nome

    def __int__(self):
        return self.id