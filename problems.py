import numpy as np


def inf_counting_audio_filesize(problems_number):
    ans = []
    freq = [16, 32, 64, 128, 192, 256]
    chan = [2, 4, 8]
    bits = [8, 16, 32]
    for i in range(problems_number):
        curr_chan = np.random.choice(chan)
        curr_freq = np.random.choice(freq)
        curr_bits = np.random.choice(bits)
        time = np.random.randint(1, 15)
        pr = "Выполнена " + str(curr_chan) + \
             "-канальная запись звука с частотой дискретизации " + str(curr_freq) + \
             "кГц и разрешением " + str(curr_bits) + " бит. Какой объем (в мегабайтах) занимает файл," \
                                                  " если запись проводилась " + str(time)
        if time < 5:
            pr += " минуты"
        else:
            pr += " минут"
        ans.append(pr)
        ans.append(curr_chan*(curr_bits/8)*curr_freq*1000*time*60//2**20)
    return ans


def inf_counting_audio_time(problems_number):
    ans = []
    freq = [16, 32, 64, 128, 192, 256]
    chan = [2, 4, 8]
    bits = [8, 16, 32]
    for i in range(problems_number):
        curr_chan = np.random.choice(chan)
        curr_freq = np.random.choice(freq)
        curr_bits = np.random.choice(bits)
        filesize = np.random.randint(100, 300)
        pr = "Выполнена " + str(curr_chan) + \
             "-канальная запись звука с частотой дискретизации " + str(curr_freq) + \
             "кГц и разрешением " + str(curr_bits) + " бит. В результате получился файл объемом " \
             + str(filesize) + " мегабайт. Определите сколько времени в секундах" \
                               " длилась запись (количество секунд - целое)"
        ans.append(pr)
        ans.append(np.around(filesize*2**23/curr_chan/curr_bits/curr_freq/1000))
    return ans


def inf_counting_image_size(problems_number):
    ans = []
    ras = {'120x180': 21600, '180*400': 72000, '400*600': 240000, '600*800': 480000, '800*1024': 819200}
    return ans


def inf_counting_image_colors(problems_number):
    ans = []
    return ans

def inf_counting_passwords():
