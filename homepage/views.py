from django.http import HttpResponse
from models import Post


def index(request):
    all_post = Post.objects.all()
    html = ''
    for post in all_post:
        html += '<a href = "' + str(post.link) + '" target = "_blank">' + post.title + '</a> published by ' + post.author + '<br>'
    return HttpResponse(html)


def detail(request, post_id):
    return HttpResponse("<h2>Details for Post Id: " + str(post_id) + " </h2>")
