import hashlib
import decorators


@decorators.logger_decor
# @decorators.logger_to_path_decor('another_log.txt')
def create_generator(file_path):
    for line in open(file_path, 'r', encoding='utf-8'):
        yield hashlib.md5(bytes(line, encoding='utf-8'))


if __name__ == '__main__':
    gen = create_generator('countries.json')
    for myhash in gen:
        print(myhash.hexdigest())
