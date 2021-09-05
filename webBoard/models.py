from django.db import models

# Create your models here.

#로그 기록 수집
class reqLog(models.Model):
    #시간/날짜
    created_at = models.DateTimeField(auto_now_add=True)
    #ip주소
    connect_ip = models.CharField(max_length=15)
    # Header | AGENT
    user_agent = models.CharField(max_length=300)
    #path * 경로
    path_info = models.CharField(max_length=500)
    #Host * 주소:포트
    host_ip_port = models.CharField(max_length=25)

#class Post(models.Model):
    #id값(자동)
    #제목
    #날짜/시간
    #내용
    #해시태그(JSON)
    #댓글(JSON)
    #댓글 개수
    #조회수 개수
    #좋아요 개수 
    