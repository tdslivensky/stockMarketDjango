from django.shortcuts import render
# api key pk_9ae92b07e8564247b862abee4f0563a6

# Create your views here.
def home(request):
	import requests 
	import json
	
	if request.method == 'POST' and request.POST['stockSearch'] != "":
		form = request.POST['stockSearch']
		apiRequest = requests.get("https://sandbox.iexapis.com/stable/stock/{0}/quote?token=Tpk_5f39a57c583b4bb4b92ce3116a2bdbdc".format(form))
		try:
			data = json.loads(apiRequest.content)
		except Exception as e:
			data = "error"
		return render(request,'home.html', {'data': data})		
	else:
		apiRequest = requests.get("https://sandbox.iexapis.com/stable/stock/AAPL/quote?token=Tpk_5f39a57c583b4bb4b92ce3116a2bdbdc")
		try:
			data = json.loads(apiRequest.content)
		except Exception as e:
			data = "error"
		return render(request,'home.html', {'data': data})


def about(request):
	return render(request,'about.html', {})
	
def addStock(request):
	return render(request,'addStock.html', {})