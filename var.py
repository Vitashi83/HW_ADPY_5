from arh import data as p
from datetime import datetime
import os


def param_logger(file_path):
    call_qty = 0

    def logger(fun):
        def new_fun(*args, **kwargs):
            nonlocal call_qty
            call_qty += 1
            result = fun(*args, **kwargs)
            now = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
            if os.path.exists(file_path):
                f_mode = 'a'
            else:
                f_mode = 'w'
            with open(file_path, f_mode) as file:
                file.write(
                    f'{call_qty}  Дата и время вызова:{now}, Имя функции: {fun.__name__}, Аргументы: {args, kwargs} | '
                    f'Возвращаемое значение: {result} \n'
                )
            return result

        return new_fun

    return logger


@param_logger('log.txt')
def salary(employees, months):
    return sum([e['salary'] * months for e in employees])


if __name__ == '__main__':
    salary(p.get_employees(), 3)
    salary(p.get_employees(), 2)

# Домашнее задание к лекции 3.«Decorators»
# 1/Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

# 2/Написать декоратор из п.1, но с параметром – путь к логам.

# 3/Применить написанный логгер к приложению из любого предыдущего д/з.