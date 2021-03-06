# coding=utf-8
"""oneingdufs.personalinfo.models 个人信息模型

@author: MoLice<sf.molice@gmail.com>
@createdate: 2012-01-30
|- AtSchool 学生行政档案数据模型
|- Student 用来实现拓展User的类
|- MyGroup 用来实现拓展Group的类
"""

from django.db import models
from django.contrib.auth.models import User
# project import
from oneingdufs.common.models import ClassList
from oneingdufs.models import *

class AtSchool(models.Model):
  """在校的个人信息，行政档案方面的"""
  # identity字段选择值
  IDENTITY_CHOICES = (
    ('0', '学生'),
    ('1', '教师'),
  )
  # 用户，与用户表关联
  userId = models.ForeignKey(User)
  # 数字广外密码
  mygdufs_pwd = models.CharField(max_length=20)
  # 出生年月
  born = models.DateField(null=True)
  # 入学年月
  enroll = models.DateField(null=True)
  # 班级，与班级表关联
  classId = models.ForeignKey(ClassList, null=True)
  # 身份
  identity = models.CharField(max_length=1, choices=IDENTITY_CHOICES, default='0')

class Student(UserExtra):
  """用户模型，以学生为角色设计
  
  扩展自django User
  """
  # 学号
  studentId = models.CharField(max_length=11, unique=True)
  # 真名
  truename = models.CharField(max_length=20, null=True) 
  # 手机
  phone= models.CharField(max_length=11, null=True)
  # 短号
  cornet = models.CharField(max_length=10, null=True)
  # qq
  qq = models.CharField(max_length=12, null=True)
  # AndroidPN用户名
  apn_username = models.CharField(max_length=32, null=True)

class MyGroup(GroupExtra):
  # 时间戳，当该Group发生变动时更新
  timestamp = models.DateTimeField(auto_now=True)
