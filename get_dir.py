import sys
import os
from collections import namedtuple
import logging


def main():
    directory_path = sys.argv[1]
    process_directory(directory_path)


MyNamedTuple = namedtuple('MyNamedTuple', ['name_of_file_or_dir', 'ext_or_flag', 'name_of_parent_dir'])

logging.basicConfig(filename='information.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='UTF-8')


def preparation_path_for_dir(directory_path):
    parent_dir_path = os.path.dirname(directory_path)
    parent_dir_name = os.path.basename(parent_dir_path)
    dir_name = os.path.basename(directory_path)
    flag_of_dir = 'dir'

    res_tuple_for_dir = MyNamedTuple(dir_name, flag_of_dir, parent_dir_name)
    return res_tuple_for_dir


def preparation_path_for_file(directory_path):
    parent_dir_path = os.path.dirname(directory_path)
    parent_dir_name = os.path.basename(parent_dir_path)
    file_name = os.path.basename(directory_path)

    file_parts = os.path.splitext(file_name)
    only_file_name = file_parts[0]
    file_extension = file_parts[1]

    res_tuple = MyNamedTuple(only_file_name, file_extension, parent_dir_name)
    return res_tuple


def process_directory(full_path):
    print(f"Обрабатываем директорию '{full_path}'", end='\n')
    for cur_dir, dirs, files in os.walk(full_path):
        for directory in dirs:
            file_tuple_dir = preparation_path_for_dir(os.path.join(cur_dir, directory))
            print(f'процесс каталога: {file_tuple_dir}')
            logging.info(file_tuple_dir)
            # нет return так как только один файл выведет

        for my_file in files:
            file_tuple_file = preparation_path_for_file(os.path.join(cur_dir, my_file))
            print(f'процесс файла {file_tuple_file}')
            logging.info(file_tuple_file)
            # нет return так как только один файл выведет


if __name__ == "__main__":
    main()
