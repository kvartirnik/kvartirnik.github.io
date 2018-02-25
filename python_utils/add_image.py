import os
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
pprint = pp.pprint
post_content = '''---
layout: default
---
![Picture example](https://raw.githubusercontent.com/kvartirnik/website/gh-pages/images/kvartirnik_photos/{}.jpg)

'''


def create_post(image):
    print(os.getcwd())
    # post_id = int(image.split('.')[0]) + 1
    image_id = str(int(image.split('.')[0]))
    post_path = '1004-' + '01-01-' + image_id + '_jpg.md'
    with open(post_path, 'w') as post:
        current_content = post_content.format(image_id)
        post.write(current_content)


def get_free_file_name():
    posts = filter(lambda x: x != '.DS_Store' or 'description' not in x,
                   os.listdir('../_posts/photogallery'))
    pprint(posts)
    posts = list(filter(lambda x: x.startswith('1004'),
                        posts))
    # last_post = max(posts)
    # lp_id = last_post[5:7]
    # print(str(int(lp_id)).zfill(2))
    images = list(filter(lambda x: x != '.DS_Store',
                         os.listdir('../images/kvartirnik_photos/')))
    print(images)
    print(posts)
    map(lambda post: os.remove('../_posts/photogallery/' + post), posts)
    os.chdir('../_posts/photogallery/')
    for image in images:
        print(image)
        create_post(image)


def add(image_title, image_path):
    pass


if __name__ == '__main__':
    get_free_file_name()
