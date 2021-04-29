from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
	html = """
	<h2>歡迎光臨何老師的網頁</h2>
	<hr>
	<a href='/'>Home</a>
	<a href='/lucky/'>Lucky</a>
	<a href='/admin/'>後台</a>
	"""
	names = ["何敏煌", "王小花", "李白", "袁枚"]
	years = range(1960, 2001)
	return render(request, "index.html", locals())

def lucky(request):
	lucky = random.randint(1, 99)
	return HttpResponse("本日幸運數字：{}".format(lucky))
