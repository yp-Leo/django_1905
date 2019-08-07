import hashlib

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User


def add(request):
    # 1.创建对象，保存到数据库
    # user = User(username='张三',password_hash=hashlib.sha1(b'123').hexdigest())
    # user.save()
    # return HttpResponse(str(user.uid))

    # 2.便捷创建 （create 创建+保存）
    # user =User.objects.create(username='单强',password_hash=hashlib(b'124').hexdigest())
    # print(res)
    # return HttpResponse(str(user.uid))

    # 3.批量创建
    tmp = []
    for i in range(10):
        user = User()
        user.username = "test"+str(i)
        user.password_hash = hashlib.sha1(str(1000+i).encode('utf8')).hexdigest()
        tmp.append(user)
    User.objects.bulk_create(tmp,batch_size=10)

    return HttpResponse("add")


def modify(request):
    # 1.修改一条记录
    # user = User.objects.get(pk=1)
    # print(user)
    # user.password_hash = hashlib.sha1(user.password_hash.encode('utf8').hexdigest())
    # user.save()

    # 2.修改多条记录
    # users = User.objects.all()
    # print(users,type(users))
    # users.update(email='123@qq.com')
    return HttpResponse('update')


def delete(request):
    # 1.删除一条记录
    # user = User.objects.get(pk=7)
    # user.delete()

    # 2.删除多条记录
    users = User.objects.filter(pk__gt=7)
    users.delete()
    print(users)

    return HttpResponse("delete")


# 查询
def find(request):
    # 1.all 获取所有记录
    # users = User.objects.all().filter(pk=1)

    #2 filter过滤，多个条件之间是逻辑与的关系
    # users = User.objects.filter(pk__lt=5,pk__gt=1)
    # users = User.objects.filter(pk__lt=5).filter(pk__gt=1)

    # 3 exlude 逻辑取反
    # users = User.objects.exclude(pk=3)

    # 4 order by排序  -开头是倒序
    # users = User.objects.all().order_by('-uid')
    # users = User.objects.all().order_by('email','-regtime')

    # 5 values 取指定字段
    users = User.objects.values('uid','username')

    # 6 valuses_list 制定字段，取出是元组
    users = User.objects.values_list('uid','username')

    # only
    users = User.objects.only('username')
    users = User.objects.defer('username')

    # 7 distinct 去除重复
    users = User.objects.values('email').distinct()
    print(users,type(users))

    return render(request,'dat/list.html',locals())


def paremeter(request):
    # 1 in
    # users = User.objects.filter(uid__in=[1,2,4,6])
    # uids = User.objects.filter(emai=None).value('uid')
    # users = User.objects.filter(uid__in=uids)

    # 3模糊查询
    users = User.objects.filter(username__icontains='tes')
    users = User.objects.filter(username__icontains='tes')
    print(users)
    return HttpResponse("参数")