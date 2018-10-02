from django.http import JsonResponse
from .posts import get_slugs, load_post


def post(request, slug):
    return JsonResponse(load_post(slug))


def posts(request):
    return JsonResponse([{'slug': slug, 'post': load_post(slug)} for slug in get_slugs()], safe=False)