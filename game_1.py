#! /usr/bin/Python
# -*- coding: UTF-8 -*-
"""
Ви́селица — игра на бумаге для двух человек.

Принцип игры
Один из игроков загадывает слово — пишет на бумаге первую и последнюю букву слова и отмечает места для остальных букв,
например чертами (существует также вариант, когда изначально все буквы слова неизвестны).
Также рисуется виселица с петлёй.

Согласно традиции русских лингвистических игр, слово должно быть именем существительным,
нарицательным в именительном падеже единственного числа,
либо множественного числа при отсутствии у слова формы единственного числа.

Второй игрок предлагает букву, которая может входить в это слово.
Если такая буква есть в слове, то первый игрок пишет её над соответствующими этой букве чертами — столько раз,
сколько она встречается в слове. Если такой буквы нет, то к виселице добавляется круг в петле, изображающий голову.
Второй игрок продолжает отгадывать буквы до тех пор, пока не отгадает всё слово.
За каждый неправильный ответ первый игрок добавляет одну часть туловища к виселице
(обычно их 6: голова, туловище, 2 руки и 2 ноги, существует также вариант с 8 частями — добавляются ступни,
а также самый длинный вариант, когда сначала за неотгаданную букву рисуются части самой виселицы).

Если туловище в виселице нарисовано полностью, то отгадывающий игрок проигрывает, считается повешенным.
Если игроку удаётся угадать слово, он выигрывает и может загадывать слово.

 ______
 |    |
 |    o
 |   /O\
 |  _/ \_
/|\
123456789
"""
import random
import os
import sys
import tkinter
import PIL


def input_letter():
    letter = '*'
    while (letter == '*'):
        letter = input('Введите букву слова:').lower()
        if (len(letter) != 1) or \
                (not letter.isalpha()) or \
                (letter in users_word) or \
                (ord(letter) < ord('а')) or \
                (ord(letter) > ord('я')):
            print('Неправильный ввод:"' + letter + '"')
            letter = '*'
    return letter


def show_status(users_word, errors_counter):
    print(''.join(users_word))
    print(f'Всего ошибок:{errors_counter}')


def can_check_word(users_word, errors_counter, MAX_ERRORS):
    return ('*' in users_word) and (errors_counter < MAX_ERRORS)


def check_word(letter, users_word, secret_word, errors_counter):
    if letter not in secret_word:
        errors_counter += 1
    else:
        for pos, char in enumerate(secret_word):
            if char == letter:
                users_word[pos] = letter


def end_game(errors_counter, MAX_ERRORS):
    if errors_counter == MAX_ERRORS:
        print('Вы проиграли')
    else:
        print('Победа!!!')


def main():
    words_list = ['автострада',
              'бензин',
              'инопланетянин',
              'самолет',
              'библиотека',
              'шайба',
              'олимпиада',
              'функционал',
              'гайка',
              'полет',
              'игра',
              'строка',
              'виселица']

    play_game = 'y'
    while play_game == 'y':
        print("Игра Виселица версия 0.1")
        secret_word = random.sample(words_list, 1)[0]
        print(secret_word)
        users_word = ['*'] * len(secret_word)
        errors_counter = 0
        MAX_ERRORS = max(8, len(secret_word))
        while can_check_word(users_word, errors_counter, MAX_ERRORS):
            show_status(users_word, errors_counter)
            letter = input_letter()
            check_word(letter, users_word, secret_word, errors_counter)

    end_game(errors_counter, MAX_ERRORS)
    play_game = input('Сыграем еще? (y/n)').lower()

if(__name__ == "__main__"):
    main()
    os.system("pause")
    quit()