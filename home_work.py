import os
import datetime
import functools

# Домашнее задание к лекции 3. «Decorators»

''' 1. Доработать декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл 'main.log' дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Функция test_1 в коде ниже также должна отработать без ошибок.'''

def logger(old_function) :
    @functools.wraps(old_function)
    def new_function(*args, **kwargs) :
        date_time_now = datetime.datetime.now()
        dt = date_time_now.date()
        tm = date_time_now.time()
        name = old_function.__name__
        arguments = f'{args}, {kwargs}'
        res = old_function(*args, **kwargs)

        

        with open('main.log', 'a') as f :
            f.write(str(dt) + '\n')
            f.write(str(tm) + '\n')        
            f.write(name + '\n')        
            f.write(arguments + '\n')        
            f.write(str(res) + '\n')        
        
        return res
    
    return new_function

@logger
def sum_num(x):
    '''функция принимает на вход строку из произвольных символов и считает сумму всех цифр в этой строке'''
    summ = 0
    for i in x :
        if i.isdigit() :
            summ += int(i)
    return summ

sum_num('123dsfasdf999sd')

def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"

    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()


''' 2. Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Путь к файлу должен передаваться в аргументах декоратора. Функция test_2 в коде ниже также должна отработать без ошибок.'''

def logger(path: str) :
    def __logger(old_function) :
        @functools.wraps(old_function)
        def new_function(*args, **kwargs) :
            date_time_now = datetime.datetime.now()
            dt = date_time_now.date()
            tm = date_time_now.time()
            name = old_function.__name__
            arguments = f'{args}, {kwargs}'
            res = old_function(*args, **kwargs)

            with open(path, 'a') as f :
                f.write(str(dt) + '\n')
                f.write(str(tm) + '\n')        
                f.write(name + '\n')        
                f.write(arguments + '\n')        
                f.write(str(res) + '\n')        

            return res

        return new_function
    return __logger



@logger('second_main.log')
def sum_num(x):
    '''функция принимает на вход строку из произвольных символов и считает сумму всех цифр в этой строке'''
    summ = 0
    for i in x :
        if i.isdigit() :
            summ += int(i)
    return summ

sum_num('123dsfasdf999sd')
        

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()

























































