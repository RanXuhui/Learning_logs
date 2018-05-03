from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # date_added是一个DateTimeField——记录日期和时间的数据，auto_now_add=True，
    # 每当用户创建新主题时，这都让Django将这个属性自动设置成当前日期和时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # 建立到模型User的外键关系

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 外键是一个数据库术语，它引用了数据库中的另一条记录
    # 书中P365原代码为topic = models.ForeignKey(Topic)系统报错
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)    # date_added让我们能够
    # 按创建顺序呈现条目，并在旁边加入时间戳

    class Meta:
        """存储用于管理模型的额外信息"""
        verbose_name_plural = 'entries'
        # 让Django在需要时使用Entries来表示多个条目，如果没有这个类，
        # Django将会使用Entries来表示多个条目

    def __str__(self):
        """返回模型的字符串表示"""
        """方法__str__()告诉Django，呈现条目时应显示哪些信息"""
        if len(self.text) > 50:
            return self.text[:50] + '...'   # 让Django只显示text的前50个字符
        else:
            return self.text
