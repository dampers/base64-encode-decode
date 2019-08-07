from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def write(request):
    return render(request, 'blog/write.html')

def error(request):
    return render(request, 'blog/error.html')

def create(request):
    blog = Blog()
    #if blog.password != '1234':
        #return render(request, 'blog/error.html')
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def ready(request):
    return render(request, 'blog/ready.html')

codesf = ['A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z','a','b','c','d',
    'e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x',
    'y','z','0','1','2','3','4','5','6','7',
    '8','9',' ','/']

def encode(request):
    full_text = request.GET['fulltext']
    msg = full_text
    lenm = len(msg)
    asc = 128
    asci = b''
    num = 0
    for i in range(lenm):
        asc = 128
        num = ord(msg[i])
        print(num)
        while asc>0:
            if num>=asc :
                num -= asc
                asci += b'1'
            else :
                asci +=b'0'
            asc //= 2
    # print(asci)
    #print(asci)
    lenb = len(asci)
    while lenb%6!=0:
        asci += '0'.encode()
        lenb = len(asci)
    print(lenb)
    word = ''
    acnt = []
    codei = []
    wcnt = 0
    k = 32
    asd = 0
    #print(asci)
    for i in range (lenb):
        acnt.append(asci[i])
        if i%6==5:
            wcnt+=1
            k = 32
            asd = 0
            for j in range(6):
                if acnt[j]==49:
                    asd += k
                k //= 2
            codei.append(asd)
            acnt.clear()

    for i in range (wcnt):
        word += codesf[codei[i]]

    for i in range(3-(lenm%3)):
        if lenm%3!=0:
            word += '='

    return render(request, 'blog/encode.html', {'fulltext':word})
