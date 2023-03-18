import numpy as np
from scipy.io.wavfile import write, read

'''Функция дискретного преобразования'''
def DFT(x):

    x = np.asarray(x, dtype=float)         # Преобразование в массив
    N = x.shape[0]                         # Количество семплов
    n = np.arange(N)                       # Массив от 0 до N - 1
    k = np.asarray([[i] for i in n])       # Массив массивов со значениями от 0 до N - 1 # k = n.reshape((N, 1))

    #M = np.exp(-2j * np.pi * k * n / N)
    furmy = []
    for i in range(N):
        matrx = []
        for j in range(N):
            m = 2.7182 ** (-2j * 3.1415 * k[i] * n[j] / N)
            matrx.append(m[0])
        furmy.append(matrx)
    furmy = np.asarray(furmy)


    #dataF = np.dot(furmy, x)
    dataF = []
    for t in range(N):
        value = 0
        for g in range(N):
            value += data[g] * furmy[g][t]
        dataF.append(value.real)
    dataF = np.asarray(dataF)

    dataF[:freq1] = 0
    dataF[freq2:] = 0
    return dataF


'''Функция обратного дискретного преобразования'''
def DFTr(y):

    N = y.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)
    g = np.dot(M, y)
    newg = []
    for i in g:
        newg.append(int((i * 1 / N).real))
    newg = np.asarray(newg)
    return newg

sample_rate, data = read('005.wav')
quan_sam = data.shape[0]
print('Частота дискретизации:', sample_rate)
print('Количество семплов:', quan_sam)
print('Продолжительность:', quan_sam / sample_rate, 'сек.')
print('Введенная частота не должна превышать', int(sample_rate / 2), 'Гц.')
freq1 = int((int(input('Введите частоту №1: ')) * quan_sam / (sample_rate / 2)) / 2)
freq2 = int((int(input('Введите частоту №2: ')) * quan_sam / (sample_rate / 2)) / 2)
if freq1 > freq2:
    freq1, freq2 = freq2, freq1



b = DFT(data)
new_sig = DFTr(b)
norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))
write("clean.wav", sample_rate, norm_new_sig)
