# -*- coding: utf-8 -*-

import StringIO
from PIL import Image, ImageDraw
import pygame
import random
import numpy as np
import card_no


def get_picture_info():
    pygame.init()

    text, captcha_text = card_no.random_text()

    bgcolor = (int(random.uniform(0, 255)), int(random.uniform(0, 255)), int(random.uniform(0, 255)))

    card_no_color = (int(random.uniform(0, 255)), int(random.uniform(0, 255)), int(random.uniform(0, 255)))

    im = Image.new("RGB", (400, 50), bgcolor)
    font = pygame.font.SysFont('Microsoft YaHei', 50)
    rtext = font.render(text, True, card_no_color, bgcolor)
    sio = StringIO.StringIO()
    pygame.image.save(rtext, sio)
    sio.seek(0)
    line = Image.open(sio)
    im.paste(line, (10, 10))

    img_d = ImageDraw.Draw(im)
    x_len, y_len = im.size
    # print im.size
    for _ in range(15):
        noise_color = (int(random.uniform(0, 255)), int(random.uniform(0, 255)), int(random.uniform(0, 255)))
        img_d.line(((random.uniform(1, x_len), random.uniform(1, y_len)),
                    (random.uniform(1, x_len), random.uniform(1, y_len))), noise_color)
    # im.save("t.jpg")

    captcha_image = np.array(im)
    return captcha_text, captcha_image


if __name__ == '__main__':
    get_picture_info()
