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


class Hangman():
    def __init__(self):
        self.errors_counter = 0
        self.Ncol = 8
        self.Nlines = 6
        self.picture = [[' '] * Ncol] * Nlines

    def show_hangman(self):
        Ncol = 8
        Nlines = 6
        if self.errors_counter == 0:
            picture = [[' ']*Ncol]*Nlines
        elif errors_counter == 1:
            picture[1][0] = '|'
            picture[1][1] = '|'
            picture[1][2] = '|'
            picture[1][3] = '|'
            picture[1][4] = '|'
        elif errors_counter == 2:
            picture[0][0] = '/'
            picture[2][0] = '\\'
        elif errors_counter == 3:
            picture[1][5] = '_'
            picture[2][5] = '_'
            picture[3][5] = '_'
            picture[4][5] = '_'
            picture[5][5] = '_'
            picture[6][5] = '_'
        elif errors_counter == 4:
            picture[6][4] = '|'
        elif errors_counter == 5:
            picture[6][3] = 'о'
        elif errors_counter == 6:
            picture[6][2] = 'О'
        elif errors_counter == 7:
            picture[5][2] = '/'
            picture[7][2] = '\\'
        elif errors_counter == 8:
            picture[5][1] = '/'
            picture[7][1] = '\\'
        elif errors_counter == 9:
            picture[4][1] = '_'
            picture[8][1] = '_'
        for i in range(Nlines):
             print(''.join(picture[i]))



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
    for i in range(10):
        show_hangman(i)
        os.system("pause")
    #main()
    os.system("pause")
    quit()