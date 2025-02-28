"""
Module: assignment1_code_sample
This module provides functions to get user input, fetch data from an API, store data in a database,
and send an email notification.
"""

import os
from urllib.request import urlopen

import pymysql



db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    """
    Prompt the user for their name and return the input.
    """
    user_input = input('Enter your name: ')
    return user_input


def send_email(to, subject, body):
    """
    Send an email using the mail command.
    """
    os.system(f'echo {body} | mail -s "{subject}" {to}')


def get_data():
    """
    Fetch data from an API endpoint and return the decoded response.
    """
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data


def save_to_db(data):
    """
    Save data to the database using a parameterized query.
    """
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
