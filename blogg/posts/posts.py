from django.conf import settings
from macpath import exists
from collections import Counter
import re

import os.path
from os import listdir


POSTS_DIR = os.path.join(settings.BASE_DIR, "assets/posts")


def get_slugs():
    return [p.split('.')[0] for p in listdir(POSTS_DIR)]


def load_post(slug):
    destination = os.path.join(POSTS_DIR, format(slug) + ".md")
    if not os.path.isfile(destination):
        raise Exception('No post with name "'+slug+'"')
    else:
        with open(destination) as f:
            content = f.read()
        tags = Counter(re.findall(r'\w+', content.lower())).most_common(5)
        return { 
            'content': content, 
            'tags': [t[0] for t in tags]
        }

