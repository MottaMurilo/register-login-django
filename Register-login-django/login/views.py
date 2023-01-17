from django.shortcuts import render, HttpResponse
import json
times = 0
def login(request):
    global times
    times += 1
    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else: report_loc = 'signin/'
    return render(request, 'login.html', {'loc':report_loc,'error': ''})
def signin(request):
    json2 = open('user_data.json',) 
    data = json.load(json2) 
    l1 = data['u_data'][0]
    emails = list(l1.keys())
    passwords = list(l1.values())
    json2.close() 
    global times
    times = times+1
    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else: report_loc = 'signin/'
    email = request.POST['email']
    password = request.POST['password']
    if email in emails:
        if passwords[emails.index(email)] == password:
            times = 0
            return HttpResponse('Você está logado!')
        else:
            return render(request, 'login.html', {'loc':report_loc,'errorclass':'alert alert-danger','error': 'Desculpe! O email ou a senha não conferem!'})
    else:
        return render(request, 'login.html', {'loc':report_loc,'errorclass':'alert alert-danger','error': 'Desculpe! Esta conta não existe, tente se registrar!'})