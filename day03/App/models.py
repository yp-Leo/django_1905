
from django.db import models

# Create your models here.
from django.utils import timezone


class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdeleted=False)


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    password_hash = models.CharField(max_length=128)
    # 用户自定义类型
    utype = ((1,'超管'),(2,'普通用户'))
    usertype = models.IntegerField(choices=utype,default=2)
    regtime = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        # 按用户名 降序排序
        # ordering = ['-username']

    # 自定义管理器，可以有多个
    objects = models.Manager()
    my_manager = UserManager()
