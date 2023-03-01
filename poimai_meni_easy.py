import time

import wrap
from wrap import world, sprite, sprite_text

wrap.add_sprite_dir("my_sprite")
world.create_world(1200, 650)
fon_sprite = sprite.add("fon", 700, 325, "fon_pacman2")
sprite.set_width_proportionally(fon_sprite, 1400)
vremi = time.time()
stop = 21

# Cоздаем пакмена
pacman = sprite.add("pacman", 100, 325, "player2")
sprite.set_size(pacman, 50, 50)

# Создаем привидение
fantom = sprite.add("privedenie", 1100, 325, "enemy_ill_blue1")
sprite.set_size(fantom, 40, 40)

# Создаем сердца
life_fantom1 = sprite.add("heart", 1170, 30)
life_fantom2 = sprite.add("heart", 1130, 30)
life_fantom3 = sprite.add("heart", 1090, 30)

#Делаем таймер
chasi = time.time()
text = time.time() - chasi
text = int(text)
text = str(text)
text2 = sprite.add_text(text, 1055, 30)

#Делаем таймер для способности
chasi_skill = time.time()
text_skill = time.time() - chasi
text_skill = int(text)
text_skill = str(text)
text2_skill = sprite.add_text(text, 300, 300)


@wrap.on_key_always(wrap.K_RIGHT, delay=15)
def povorot_right():
    get_pacman = sprite.get_angle(pacman)
    sprite.set_angle(pacman, get_pacman + 10)


@wrap.on_key_always(wrap.K_LEFT, delay=15)
def povorot_left():
    get_pacman = sprite.get_angle(pacman)
    sprite.set_angle(pacman, get_pacman - 10)


def top_stop():
    top_fantom = sprite.get_top(fantom)
    if top_fantom < 0:
        sprite.move_to(fantom, sprite.get_x(fantom), 20)


def bottom_stop():
    bottom_fantom = sprite.get_bottom(fantom)
    if bottom_fantom > 650:
        sprite.move_bottom_to(fantom, 650)


def left_stop():
    left_fantom = sprite.get_left(fantom)
    if left_fantom < 0:
        sprite.move_left_to(fantom, 0)


def right_stop():
    right_fantom = sprite.get_right(fantom)
    if right_fantom > 1200:
        sprite.move_right_to(fantom, 1200)


@wrap.always(10)
def move_prizrak(pos_x, pos_y):
    sprite.move_at_angle_point(fantom, pos_x, pos_y, 4)
    top_stop()
    bottom_stop()
    left_stop()
    right_stop()


@wrap.always(50)
def move_pacman():
    if sprite.get_costume(fantom) == "enemy_ill_blue1":
        sprite.move_at_angle_dir(pacman, 12)
        sprite.set_angle_to_point(pacman, sprite.get_x(fantom), sprite.get_y(fantom))


@wrap.on_key_down(wrap.K_t)
def invisible_true():
    global vremi
    sprite.set_costume(fantom, "enemy_inv")
    vremi = time.time()


@wrap.always
def proverka_invisible():
    if sprite.get_costume(fantom) == "enemy_inv":
        time_invisible = time.time() - vremi
        if time_invisible > 3.0:
            sprite.set_costume(fantom, "enemy_ill_blue1")  #<- Фантом выходит из невидимости


@wrap.always
def taimer():
    text = time.time() - chasi
    text = int(text)
    text = str(text)
    sprite_text.set_text(text2, text)

@wrap.always
def taimer_skill():
    text_skill = time.time() - chasi_skill
    ostaloci = 21 - text_skill
    ostaloci = int(ostaloci)
    ostaloci = str(ostaloci)
    sprite_text.set_text(text2_skill, ostaloci)

@wrap.on_key_down(wrap.K_6)
def stop_taimer():
    global stop


# Нужен таймер в обратную сторону
# №1 Таймер который ведёт обратный отсчет от 20 до 0. #Сделано
# №2 Отсчёт должен начинаться когда Фантом вышел из невидимости.

###Состояния таймера
# Таймер в начале стоит на месте.
##Собятие Фантои вышел из невидимости
# Таймер ведёт отсчёт от 20 до 0
##Событие Таймер досчитал до цифры 0
# Таймер стоит