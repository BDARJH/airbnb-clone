from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  # 생성된 날짜
    updated = models.DateTimeField(auto_now=True)  # 업데이트 날짜

    class Meta:
        abstract = True  # 데이터베이스에는 나타나지 않는 모델 (추상)
