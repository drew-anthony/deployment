from django.shortcuts import render, HttpResponse, redirect

def index(req):
    print('check')
    return render(req, 'index.html')

def buy(req):
    print('checked')
    items = {
        "shirt": 19.99,
        "sweater": 29.99,
        "cup": 4.99,
        "book": 49.99
    }
    if not "total" in req.session:
        req.session['total'] = 0
    if not 'itemcount' in req.session:
        req.session['itemcount'] = 0
    print(req.POST['item'])
    price = items[req.POST['item']]
    
    req.session['price'] = price*float(req.POST['quantity'])
    req.session['total'] = req.session['total'] + price*float(req.POST['quantity'])
    print(req.session['total'])
    req.session['itemcount'] += 1*int(req.POST['quantity'])
    return redirect('/checkout')

def checkout(req):
    return render(req, 'checkout.html')

def reset(req):
    print('checcccc')
    req.session.clear()
    return redirect('/')
