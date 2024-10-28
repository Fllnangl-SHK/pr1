import sys
import subprocess
import getpass
import random
import os
import time

def out_red(text):
    print("\033[31m{}".format(text))

def out_lightblue(text):
    print("\033[1m\033[36m{}".format(text))

def out_black(text):
    print("\033[30m{}".format(text))

def out_green(text):
    print("\033[32m{}".format(text))

def out_purple(text):
    print("\033[35m{}".format(text))

def out_classic(text):
    print("\033[0m{}".format(text))




out_red('WARNING')
time.sleep(2)
out_red('''The developer of this game does not bear any responsibility for the plot of this game and for all user actions.

This is just a game and is intended for entertainment purposes only.

This game contains materials that are not recommended for children and people who support LGBTQ+,
the author of the game does not support or promote anything, for him there are only two genders,
male and weak.

At the moment the game is at an early stage of development, remember this if you encounter any errors
''')
time.sleep(10)
os.system('cls')
time.sleep(1)
out_lightblue('RUS.EMPIRE GAMES presents')
time.sleep(5)
os.system('cls')
time.sleep(3)
out_green('chapters marked in green are text chapters')
out_red('chapters marked in red are interactive chapters')
time.sleep(10)
os.system('cls')
time.sleep(3)
out_red('Welcome to RE:LIFE')
time.sleep(3)
out_classic('press 1 + Enter for start Life')
start = int(input())

if start == 1:
    out_classic('Select the game language:')
    out_red('1 - English')
    out_lightblue('2 - Russian')
    lg = int(input())

if lg == 1:
    out_classic('Sorry, this language will be added in next update')
    out_classic('Select the game language:')
    out_red('1 - English')
    out_lightblue('2 - Russian')
    lg = int(input())
    if lg == 1:
        out_classic('''
        Sorry, this language will be added in next update.
        Russian language will be forcibly selected
        ''')
    elif lg == 2:
        out_classic('Выбран русский язык')
elif lg == 2:
    out_classic('Выбран русский язык')
time.sleep(5)
os.system('cls')
time.sleep(3)
out_green('Глава 1 часть 1: Прошлая жизнь')
time.sleep(3)
out_classic('02.05.2024 6:01 Четверг')
time.sleep(3)
out_classic('Ранее утро.')
time.sleep(3)
out_classic('Тёплые лучи солнца незванно проходили сквозь окно и окутывали всю комнату.')
time.sleep(3)
out_classic('Птичий звон раздавался с улицы, проникая через приоткрытую форточку.')
time.sleep(3)
out_classic('А будильник вновь предательски кричал.')
time.sleep(3)
out_green('-...')
time.sleep(3)
out_green('-...')
time.sleep(3)
out_red("- АААААА, да замолчи же уже!!!")
time.sleep(3)
out_green("- ещё одно бессмысленное утро.")
time.sleep(3)
out_green("- ладно, пора вставать и собираться на эту чёртову работу...")
time.sleep(3)
out_classic("Попав на кухню передо мной предстала картина напоминавшая о моей никчёмности")
time.sleep(3)
out_classic('''Стол был весь в мусоре, раковина была переполнена грязной посудой,
а в холодильнике уже давно повесилась мышь''')
time.sleep(3)
out_green('- пора бы уже давно прибраться здесь, но пожалуй не сегодня.')
time.sleep(3)
out_classic('''Съев, купленную на последние деньги, булочку с маком и запив всё это чаем
я отправился в ванную''')
time.sleep(3)
out_classic("Здесь картина была не лучше")
time.sleep(3)
out_classic("Раковина уже давно была залита чем-то неизвестного происхождения")
time.sleep(3)
out_classic("С потолка капала вода")
time.sleep(3)
out_classic("А моё отражение в зеркале уже давно скрылось за слоем грязи и разводов")
time.sleep(3)
out_green("1 - Умыться и уйти из ванной")
out_red("2 - Протереть зеркало и взгялунть на себя")
fi = int(input())
if fi == 1:
    out_classic("Закончив с водными процедурами я направился в свою комнату надевать свой костюм")
    time.sleep(3)
elif fi == 2:
    out_green("- ну и рожа, лучше бы никогда её не видел")
    time.sleep(3)
    out_classic("Закончив с водными процедурами я направился в свою комнату надевать свой костюм")
    time.sleep(3)
out_classic("Зайдя в комнату мой взгляд упал на рамку с фотографией стоящей на полке")
time.sleep(3)
out_lightblue("- какой же красивой она была...")
time.sleep(3)
out_lightblue("- жаль, что мы расстались именно на такой ноте...")
time.sleep(3)
out_classic("Закончив собираться я снова взглянул на свою берлогу и закрыв дверь отправился на работу")
time.sleep(3)
os.system('cls')
time.sleep(5)
out_green("Глава 1 часть 2: Последняя встреча")
time.sleep(3)
out_classic('02.05.2024 19:32 Четверг')