# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.

with open('file.txt', 'w') as data:
    data.write('-2\n')
    data.write('8\n')
    data.write('5\n')
    data.write('6\n')
    data.write('10\n')


def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def get_mult(numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult

path = 'file.txt'

datalist = get_data_from_file(path)

print(datalist)
print(get_mult)

