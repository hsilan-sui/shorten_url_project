from django.db import models
from django.utils import slugify

# Create your models here.
class Link(models.Model):
        name = models.CharField(max_length=50,unique=True)
        url = models.URLField(max_length=200) # URLField =>確保url是有效的
        slug = models.SlugField(unique=True, blank=True) #特殊的字段類型，用於存儲 URL 友好的短標識符，即 slug。這個字段通常用於生成簡潔、可讀的 URL 路徑
        clicks = models.PositiveIntegerField(default=0)

        def __str__(self):
            #讓admin的dashboard的link object有語意
            return f"{{self.name}} | {{self.clicks}}"
        
        #創建方法，讓模型和模型能夠交互作用 
        #每當有人點擊 ＝> click就會自增 =>存進資料庫
        def click(self):
            self.click += 1
            self.save()# 存進資料庫

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name) #使用 Django 的 slugify 函數將字串轉換為 URL 友好的格式
            
            return super().save(*args, **kwargs)