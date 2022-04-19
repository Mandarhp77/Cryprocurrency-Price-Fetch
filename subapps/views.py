from django.shortcuts import redirect, render
import ccxt, time
import gate_api
from gate_api.api.spot_api import SpotApi
import threading
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def price(request):
    exchange = ccxt.gateio()
    markets = exchange.fetch_markets()

    if request.method =="POST":
        IP = request.POST['price']
        symbol = (f'{IP}/USDT')
        symbols = [symbol for symbol in [market['symbol'] for market in markets]]

        if symbol in symbols:
            messages.success(request," Entered  Coin is Availble")   
        else:
            messages.error(request, " Unfortunately, Entered  Coin is not listed")
            return redirect('price')
            

        def check():
            check.rate = exchange.fetch_ticker(symbol)['last']

        def time(): 
            if symbol in symbols:
                threading.Timer(2, time).start()
                check()
        time()
        result=[]
        context ={
            'rate': check.rate,
            'coin': symbol
        }
        result.append(context)

        return render(request, 'price.html', {'result' : result})
    return render(request, 'price.html')
