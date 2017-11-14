# ProjectX
这是一个简单的爬虫，可以从http://china.caixin.com/anticorruption-list/ 爬取内容

# 执行爬虫程序：
  在ProjectX文件夹下，执行命令
    ```scrapy crawl caixins```
      
## 几点说明：

* 首次执行之前可能要配置环境，应该不是太复杂，
  参考https://docs.scrapy.org/en/latest/intro/install.html，特别是Mac OS X 章节
* 只有caixin/spiders/lovely_spider.py是真正自己写的，其它的都是follow 
  https://docs.scrapy.org/en/latest/intro/tutorial.html 生成；
* 这只是一个简单版本，可以扒下caixin列表的第一页（25条）；结果被以UTF-8编码写
  入一个csv文件，可以用excel以导入（数据->自文件）形式打开（直接打开可能是乱码）
* 如果这是符合要求的，我们再扩展到全部的网页；并且设置爬取速度等

