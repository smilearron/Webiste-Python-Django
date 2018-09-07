from django.shortcuts import render
from . import forms
import smtplib
import email.mime.multipart
import email.mime.text


# Create your views here.
msgFrom = 'zhengjianian@163.com' #从该邮箱发送
msgTo = '981951156@qq.com' #发送到该邮箱
smtpSever='smtp.163.com' # 163邮箱的smtp Sever地址
smtpPort = '25' #开放的端口
sqm='199488jy' # 在登录smtp时需要login中的密码应当使用授权码而非账户密码

def index(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print('VALIDATION SUCCESS!')

            # DO SOMETHING CODE
            msg = email.mime.multipart.MIMEMultipart()
            #msgFrom = form.cleaned_data['email']
            name = form.cleaned_data['name']
            mail = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            content = 'You receive a new message from '+ name +'. Detailed information: \n'
            content += 'Name: ' + name + '\n'
            content += 'Email: ' + mail + '\n'
            content += 'Message: \n'
            content += message
            msg['from'] = msgFrom
            msg['to'] = msgTo
            msg['subject'] = subject
            txt = email.mime.text.MIMEText(content)
            msg.attach(txt)
            smtp = smtplib
            smtp = smtplib.SMTP()

            smtp.connect(smtpSever, smtpPort)
            smtp.login(msgFrom, sqm)
            smtp.sendmail(msgFrom, msgTo, str(msg))

            smtp.quit()


    return render(request, 'sail_app/index.html', {'form':form})

def news(request):
    return render(request, 'sail_app/news.html')

def member(request):
    return render(request, 'sail_app/member.html')

def publications(request):
    return render(request, 'sail_app/publications.html')

def course(request):
    return render(request, 'sail_app/course.html')

def students(request):
    return render(request, 'sail_app/students.html')

def opportunities(request):
    return render(request, 'sail_app/k12opportunities.html')

def research1(request):
    return render(request, 'sail_app/research1.html')

def research2(request):
    return render(request, 'sail_app/research2.html')

def research3(request):
    return render(request, 'sail_app/research3.html')

def research4(request):
    return render(request, 'sail_app/research4.html')

def partner(request):
    return render(request, 'sail_app/partner.html')
