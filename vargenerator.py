import subprocess as sb
from problems import *


def gen_var(varnum=1):
    answers = []
    fname = 'res' + str(varnum) + '.tex'
    res = open(fname, 'w')
    res.write('\documentclass[a4paper,report,14pt]{ncc}\n')
    res.write(r'\usepackage[utf8]{inputenc}' + '\n')
    res.write(r'\usepackage[T2A]{fontenc}' + '\n')
    res.write(r'\usepackage[russian]{babel}' + '\n')
    res.write(r'\usepackage{indentfirst}' + '\n')
    res.write(r'\usepackage{textcomp}' + '\n')
    res.write(r'\setcounter{secnumdepth}{1}' + '\n\n')
    res.write(r'\begin{document}' + '\n')
    res.write(r'\begin{center}' + '\n')
    res.write('Вариант ' + str(varnum) + '\n')
    res.write(r'\end{center}' + '\n')

    #res.write('Найдите основание системы счисления, для которой выполнено сложение:\n')
    #res.write(r'\begin{enumerate}' + '\n')
    #for i in range(0, 15):
    #    base = np.random.randint(4, 21)
    #    while base == 10:
    #        base = np.random.randint(4, 21)
    #    answers.append(base)
    #    x = np.random.randint(10, 200)
    #    y = np.random.randint(20, 300)
    #    res.write(r'\item ' + str(convert_base(x, to_base=base)) + ' + ' + str(convert_base(y, to_base=base)) + ' = ' +
    #              str(convert_base(x+y, to_base=base)) + '\n')

    #res.write(r'\end{enumerate}' + '\n')

    #res.write('Определеите основание системы счисления N:\n')
    #res.write(r'\begin{enumerate}' + '\n')
    #for i in range(0, 15):
    #    base = np.random.randint(4, 18)
    #    while base == 10:
    #        base = np.random.randint(4, 18)
    #    answers.append(base)
    #    x = np.random.randint(60, 300)
    #    conv_x = convert_base(x, base)
    #    res.write(r'\item' + 'Запись числа $' + str(x) + '_{10}$ в системе счисления с основанием N оканчивается на '
    #              + conv_x[-1:] + ' и содержит ' + str(len(conv_x)) + ' цифры \n')

    #res.write(r'\end{enumerate}' + '\n')
    res.write('Осуществите перевод:')
    res.write(r'\begin{enumerate}' + '\n')
    for x in range(0, 30):
        base_from = [3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15]
        base_to = [2, 8, 10, 16]
        question, ans = numeric_notation_convert_number(np.random.choice(base_from), np.random.choice(base_to))
        answers.append(ans)
        res.write(question)
    res.write(r'\end{enumerate}')

    res.write('Решите следующие задачи:')
    res.write(r'\begin{enumerate}' + '\n')
    for x in range(0, 20):
        if x % 2 == 0:
            question, ans = inf_counting_audio_time()
        else:
            question, ans = inf_counting_audio_filesize()
        answers.append(int(ans))
        res.write(question)
    for x in range(0, 20):
        question, ans = inf_counting_passwords(np.random.randint(30,70))
        answers.append(int(ans))
        res.write(question)
    res.write(r'\end{enumerate}')


    res.write(r'\newpage' + '\n') # помещаем с новой страницы все ответы
    for ans in range(len(answers)):
        res.write(str(ans + 1) + '  ' + str(answers[ans]) + '\n\n')
    res.write(r'\end{document}')
    res.close()
    sb.run('pdflatex ' + fname, shell=True)
    sb.run('pdflatex ' + fname, shell=True)
    return
