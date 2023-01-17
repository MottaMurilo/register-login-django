from django.shortcuts import render, HttpResponse
from django.urls import resolve
import json
times = 0
def register(request):
    global times
    times += 1
    current_url = request.path
    if request.path == '/register/signup/':
        report_loc = '../signup/'
    else: report_loc = 'signup/'
    return render(request, 'register.html', {'loc':report_loc,'error': ''})
def signup(request):
    if request.path == '/register/signup/':
        report_loc = '../signup/'
    else: report_loc = 'signup/'
    json2 = open('user_data.json',) 
    data = json.load(json2) 
    l1 = data['u_data'][0]
    emails = list(l1.keys())
    passwords = list(l1.values())
    json2.close() 

    email = request.POST['email']
    password = request.POST['password']
    password1 = request.POST['password1']
    usernames = []
    if email not in emails:
        if password == password1:
            emails.append(email)
            passwords.append(password)
            d4 = {emails[len(emails)-1]: passwords[len(emails)-1]}
            for x in range(len(emails)-1):
                d4 = dict(list(d4.items()) + list({emails[x]:passwords[x]}.items()))
            json_object = '{"u_data": ['+json.dumps(d4, indent = 4)+']}'
            a = open('user_data.json', 'w')
            a.write(json_object)
            a.close()
            times = 0
            return HttpResponse('Você está registrado!')
        else:
            return render(request, 'register.html', {'loc':report_loc,'errorclass':'alert alert-danger','error': 'Desculpe! O email ou a senha não conferem!'})
    else:
        return render(request, 'register.html', {'loc':report_loc,'errorclass':'alert alert-danger','error': 'O Email ou o username já estão em uso!'})