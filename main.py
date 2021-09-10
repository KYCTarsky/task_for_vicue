'''made by kyct_2018@mail.ru'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python ver 3.7

import sys
import os
import base64
import re
import json


def decode_base64_data(filename: str ='file.txt'):
    '''
    decode_base64_data do:
    1)open file.txt with text on base64
    2)decode him in str
    3)convert in dict
    4)return data
    '''

    try:
        with open(os.path.abspath(filename)) as crypt_file:
            file = crypt_file.read()
            pre_file = re.sub('\n', '', file)
            base64_bytes = base64.b64decode(pre_file)
            base64_bytes = base64_bytes.decode('utf-8')
            base64_bytes = json.loads(base64_bytes)
    except IOError:
        print('Файл не найден. Проверьте правильность ввода.')
        sys.exit()

    return base64_bytes

def search_customers(car_and_cus_data:dict):
    '''
    :param car_and_cus_data:
    :return:
    '''
    car_list = car_and_cus_data.get('cars')
    customers_list = car_and_cus_data.get('customers')

    for car_data in car_list:
        for customer_data in customers_list:
            if car_data.get('price')/100 <= customer_data.get('balance'):
                print('Car {} {} can be offered for {} {}.'.format(car_data.get('brand'),
                                                                   car_data.get('model'),
                                                                   customer_data.get('firstname'),
                                                                   customer_data.get('lastaname'))
                        )
                #Car <brand> <model> can be offered for <firstname> <lastname>.

def main():
    '''main define'''
    car_and_cus_dict = decode_base64_data()
    search_customers(car_and_cus_dict)

if __name__ == '__main__':
    main()
