#!/usr/bin/env python3

import os
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def print_status(x):
    # print("\n")
    print(x)
    # print("\n")
    
def print_problem(x):
    print("-----------------------------------------")
    print(x)
    print("-----------------------------------------")
  
def create_if_not_exists(d):
    if not os.path.exists(d):
        os.makedirs(d)
    
def ensure_dirs(dir_to_grade, dir_alr_graded, tp_ws, num_of_exercises):
    for d in [dir_alr_graded, dir_to_grade]:
        create_if_not_exists(d)
    exs_to_grade_dirs, exs_alr_graded_dirs = list(), list()
    for exercise in tp_ws['B1':colnum_string(num_of_exercises+1)+'1'][0]:
        exs_to_grade_dirs.append(os.path.join(dir_to_grade, exercise.value))
        exs_alr_graded_dirs.append(os.path.join(dir_alr_graded, exercise.value))
        for d in [exs_to_grade_dirs[-1], exs_alr_graded_dirs[-1]]:
            create_if_not_exists(d)
    return exs_to_grade_dirs, exs_alr_graded_dirs