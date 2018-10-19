#!/usr/bin/env python3

import sys
import urllib.request
from urllib.error import HTTPError
import os

base_url = 'https://api.github.com/repos/Purdue-CS193/lab-4-{}/contents/answers.txt'  # replace with proper url
token = 'Your_Token_Here'  # fill in your GitHub personal token
# token = input('Enter your GitHub personal token:')

with open('github_usernames.txt', mode='r') as username_file:
    usernames = username_file.read().splitlines()

grade_file = open('grades.txt', mode='x')  # will throw exception if the file exists, prevent overwriting
grades = []

for username in usernames:
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the terminal buffer
    print('Showing contents for', username)
    print('\n======================================================\n')

    url = base_url.format(username)
    request = urllib.request.Request(url)
    request.add_header('Authorization', 'token %s' % token)
    request.add_header('Accept', 'application/vnd.github.v3.raw')
    try:
        with urllib.request.urlopen(request) as response:
            contents = response.read()
            print(contents.decode("utf-8"))
    except HTTPError as e:
        print(e, file=sys.stderr)
        print('Marked as NOT_FOUND')
        grades.append('NOT_FOUND\n')
        input('Press any key to continue')
        continue

    print('\n======================================================\n')
    score = input('Enter the grade:')
    grades.append(str(score) + '\n')

assert len(usernames) == len(grades)  # sanity check
grade_file.writelines(grades)
grade_file.close()
