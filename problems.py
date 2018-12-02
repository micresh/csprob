import numpy as np
from supplyfunctions import convert_base


def inf_counting_audio_filesize(max_minutes = 15):
    freq = [16, 32, 64, 128, 192, 256]  # доступные частоты
    chan = [2, 4, 8]  # доступное количество каналов
    bits = [8, 16, 32]  # доступное разрешение канала записи
    curr_chan = np.random.choice(chan)
    curr_freq = np.random.choice(freq)
    curr_bits = np.random.choice(bits)
    time = np.random.randint(1, max_minutes)
    pr = r"\item " + "Выполнена " + str(curr_chan) + \
         "-канальная запись звука с частотой дискретизации " + str(curr_freq) + \
         "кГц и разрешением " + str(curr_bits) + " бит. Какой объем (в мегабайтах) занимает файл," \
                                                 " если запись проводилась " + str(time)
    if time < 5:
        pr += " минуты"
    else:
        pr += " минут"
    return pr, curr_chan * (curr_bits / 8) * curr_freq * 1000 * time * 60 // 2 ** 20


def inf_counting_audio_time(min_fs = 5, max_fs=100):
    freq = [16, 32, 64, 128, 192, 256]
    chan = [2, 4, 8]
    bits = [8, 16, 32]
    curr_chan = np.random.choice(chan)
    curr_freq = np.random.choice(freq)
    curr_bits = np.random.choice(bits)
    fs = np.random.randint(min_fs, max_fs)
    pr = r"\item " + "Выполнена " + str(curr_chan) + \
         "-канальная запись звука с частотой дискретизации " + str(curr_freq) + \
         "кГц и разрешением " + str(curr_bits) + " бит. В результате получился файл объемом " \
         + str(fs) + " мегабайт. Определите сколько времени в секундах" \
                     " длилась запись (количество секунд - целое)"

    return pr, np.around(fs * 2 ** 23 / curr_chan / curr_bits / curr_freq / 1000)


def inf_counting_image_size():
    ans = []
    ras_lines = [120, 180, 240, 360, 480, 600, 800]
    ras_rows = [120, 180, 240, 360, 480, 600]
    return ans


def inf_counting_image_colors():
    ans = []
    return ans


def inf_counting_passwords(pass_count):
    alph_length = np.random.randint(20, 48)
    pass_length = np.random.randint(6, 18)
    bits = np.log2(alph_length)
    if bits != int(bits):
        bits = int(bits) + 1
    else:
        bits = int(bits)
    bites = pass_length * bits
    if bites % 8 == 0:
        bites //= 8
    else:
        bites = bites // 8 + 1
    ans = pass_count * bites
    pr = r"\item Для регистрации на сайте пользователю необходимо придумать пароль, состоящий из " \
         + str(pass_length) + " символов. В качестве символов используются десятичные цифры и " + str(alph_length - 10)\
         + " различных букв местного алфавита. Под хранение каждого пароля отводится минимально возможное " \
           "целое количество байт, при этом кодирование символов осуществляется равномерным и минимально возможным " \
           "количеством бит. Определите объем памяти в байтах, который занимает хранение " + str(pass_count)\
         + " паролей."

    return pr, ans


def numeric_notation_convert_number(from_base=10, to_base=2, min_number=20, max_number=500):
    gen_number = np.random.randint(min_number, max_number)
    res_number = convert_base(gen_number, to_base)
    pr = r"\item " + "$ " + convert_base(gen_number, from_base) + \
         "_{" + str(from_base) + "} = X_{" + str(to_base) + "}$"
    return pr, res_number

