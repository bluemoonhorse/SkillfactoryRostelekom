"""Действующие данные для авторизации в системе"""
import os
from dotenv import load_dotenv
from faker import Faker
import string
load_dotenv()


"""искусственные данные для авторизации в системе"""
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()
fake_password = fake.password()
fake_login = fake.user_name()
fake_email = fake.email()


"""сюда реальные данные для авторизации в системе"""
"""os.environ['phone'] = 'qwe'  """
"""os.environ['login'] = 'qwe'   """
"""os.environ['password'] = 'qwe'   """

valid_phone = os.getenv('phone')
valid_login = os.getenv('login')
valid_password = os.getenv('password')
invalid_ls = '352012341234'

valid_email = '7m079dekkp@wuuvo.com'
valid_pass_reg = '6!4@%eSoQL'


def generate_string_rus(n):
    return 'я' * n


def generate_string_en(n):
    return 'z' * n


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():    # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return f'{string.punctuation}'
