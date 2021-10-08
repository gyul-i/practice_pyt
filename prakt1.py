import os
import shutil
import zipfile

if not os.path.isdir("work_here"):
     os.mkdir("work_here")
os.chdir("work_here")
print('вы находитесь в рабочей папке')

def make_file(): # создание файла и запись текста в файл
    s = str(input('введите название файла, который хотите создать: '))
    file = open(s, "w")
    q = str(input('вы хотите записать что-то в файл? да/нет '))
    if q == 'да' or q == 'yes':
        text=str(input('записывайте:  '))
        file.write(text)
        file.close()
        print('текст записан в файл')
        return
    elif q == 'нет' or q == 'no':
        file.close()
        return
    else:
        file.close()
        print('ошибка')
        return

def mk(): # создание папки
    s = str(input('введите название папки, которую хотите создать: '))
    os.mkdir(s)
    print('папка создана')
    return

def de(): # удаление папки
    os.rmdir(str(input('какую директорию вы хотите удалить?')))
    print('директория удалена')
    return

def ch(): # перемещение в другую папку
    print('примечание: перемещайтесь только внутри рабочей папки ')
    os.chdir(str(input('введите название папки, в которую хотите переместиться: ')))
    print("Текущая директория изменилась: ", os.getcwd())
    return

def de_file(): #удаление файла
    file = str(input('введите название файла, который хотите удалить: '))
    os.remove(file)
    print('файл удален')
    return

def rep_file(): #перемещение файла
    s = str(input('введите название файла, который хотите переместить: '))
    t = str(input('папка, в которую вы хотите переместить файл и название файла. пример: папка/файл '))
    file = open(s, "w")
    file2 = open(t, "w")
    os.replace(file,file2)
    file.close()
    file2.close()
    print('файл перемещен')
    return

def read_file(): #чтение файла
    file = open(str(input('имя файла, который хотите прочитать: ')), "r")
    print(*file)
    #file.read()
    file.close()
    return


def rename_file(): #переименование файла
    s = str(input('введите название файла, который хотите переименовать: '))
    t = str(input('введите его новое имя'))
    os.rename(s,t)
    return 'файл переименован'

def cop_file(): #файл скопирован
    s = str(input('введите название файла, который хотите копировать: '))
    t = str(input('введите имя файла, в который хотите копировать: '))
    shutil.copyfile(s,t)
    return "файл скопирован"



def arhiv(): #архивирование файла (доп. задание)
    z = zipfile.ZipFile(str(input("какое будет название сжатого файла"))+".zip", 'w')
    z.write(str(input('название файла, который собираетесь сжимать')), compress_type=zipfile.ZIP_DEFLATED)
    z.close()

def izvl(): #извлечение файла (доп. задание)
    xz = zipfile.ZipFile(str(input('введите zip файл')))
    xz.extractall(str(input('куда поместить файл')))
    xz.close()

n=''
while n!='exit':
    print('меню')
    print('1.Создание папки (с указанием имени)')
    print('2.Удаление папки по имени')
    print('3.Перемещение между папками')
    print('4.Создание пустых файлов с указанием имени. Запись текста в файл')
    print('5.Просмотр содержимого текстового файла')
    print('6.Удаление файлов по имени')
    print('7.Копирование файлов из одной папки в другую')
    print('8.Перемещение файлов')
    print('9.Переименование файлов')
    print('10.Архивирование файлов (доп задание)')
    print('11.Извлечение файлов (доп задание)')
    print('exit')
    n=input('введите номер пункта')
    if n == '1':
        mk()
    elif n == '2':
        de()
    elif n == '3':
        ch()
    elif n == '4':
        make_file()
    elif n == '5':
        read_file()
    elif n == '6':
        de_file()
    elif n == '7':
        cop_file()
    elif n == '8':
        rep_file()
    elif n == '9':
        rename_file()
    elif n == '10':
        arhiv()
    elif n == '11':
        cop_file()
    elif n=="exit":
        break
    else:
        print('ошибка при ввооде')