# goby爬虫使用说明

效果展示

![image-20240319221550955](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240319221550955.png)

![image-20240321160608360](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240321160608360.png)



开发环境

```
python3.8
```

测试环境

```
python3.7-3.9
```



使用

```
python .\goby_spider.py -h
```



注意事项

```
1.只能爬取2023年到现在的漏洞
2.爬取文件在对应data目录下
3.尽量在config.py中填入cookie，避免被识别为爬虫
```





### 安装

可以使用如下命令安装依赖库：

```plaintext
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```





关注公众号回复 goby爬虫 获取工具
