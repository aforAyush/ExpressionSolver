from django.shortcuts import render

def index_view(request):
    contect_dict = {}
    if 'submit' in request.POST:
        try:
            exp = request.POST['exp']
            ans = eval(exp)
            nameError = False
            contect_dict = { 'nameError':nameError ,'ans':ans, 'exp':exp}
        except NameError:
            nameError = True
            ans = ""
            contect_dict = { 'nameError':nameError ,'ans':ans, 'exp':exp}
    return render(request,'index.html',contect_dict)