import os
import time


def logger_decor(in_func):
    path = os.path.join(os.getcwd(), 'log.txt')

    def new_func(*args, **kwargs):
        current_time = time.gmtime(time.time())
        str_time = time.strftime('%d.%m.%Y %X', current_time)

        with open(path, 'a', encoding='utf-8') as f:
            f.write(
                f'''{str_time}:
                Called func {in_func.__name__}
                with args: {args}, kwargs: {kwargs}\n'''
            )
        return in_func(*args, **kwargs)

    return new_func


def logger_to_path_decor(path):
    def logger_decor(in_func):
        def new_func(*args, **kwargs):
            current_time = time.gmtime(time.time())
            str_time = time.strftime('%d.%m.%Y %X', current_time)

            with open(path, 'a', encoding='utf-8') as f:
                f.write(
                    f'''{str_time}:
                    Called func {in_func.__name__}
                    with args: {args}, kwargs: {kwargs}\n'''
                )
            return in_func(*args, **kwargs)

        return new_func

    return logger_decor


if __name__ == '__main__':

    @logger_decor
    def mysum(a, b):
        return a + b

    @logger_to_path_decor('another_log.txt')
    def mymul(a, b):
        return a * b

    print(mysum(2, 3))
    print(mysum(3, 1))
    print(mysum(5, 6))
    print(mymul(2, 3))
    print(mymul(3, 1))
    print(mymul(5, 6))