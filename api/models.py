from django.db import models
from django.contrib.auth import User

# Create your models here.

class Todo(models.Model):
	id =  models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField()
	feed = models.ForeignKey(Feedback,on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.name} du {self.start_date} au {self.end_date}"

class Employe(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	role = models.CharField(max_length=50,editable=False,null=False)
	task = models.ForeignKey(Todo,on_delete=models.PROTECT)

	def __str__(self):
		return f'{self.user.username} {self.role}'

class Feedback(models.Model):
	id = models.AutoField(primary_key=True)
	feed = models.TextField(blank=False)
	task = models.ForeignKey('Todo',on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.feed} {self.task.name}"
