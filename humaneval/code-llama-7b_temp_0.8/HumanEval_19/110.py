from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list) - i - 1):
            if 'zero' in numbers_list[j] or numbers_list[j] in ('one', 'two', 'three', 'four', 'five'):
                if 'zero' in numbers_list[j + 1] or 'one' in numbers_list[j + 1] or 'two' in numbers_list[j + 1] or 'three' in numbers_list[j + 1] or 'four' in numbers_list[j + 1] or 'five' in numbers_list[j + 1]:
                    if numbers_list[j] in ('zero', 'one', 'two', 'three', 'four', 'five'):
                        if numbers_list[j] in ('one', 'two', 'three', 'four', 'five'):
                            if numbers_list[j] in ('two', 'three', 'four', 'five'):
                                if numbers_list[j] in ('three', 'four', 'five'):
                                    if numbers_list[j] in ('four', 'five'):
                                        if numbers_list[j] in ('five'):
                                            continue
                        if numbers_list[j + 1] in ('one', 'two', 'three', 'four', 'five'):
                            if numbers_list[j + 1] in ('two', 'three', 'four', 'five'):
                                if numbers_list[j + 1] in ('three', 'four', 'five'):
                                    if numbers_list[j + 1] in ('four', 'five'):
                                        if numbers_list[j + 1] in ('five'):
                                            numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
                                            continue
                    else:
                        if numbers_list[j + 1] in ('one', 'two', 'three', 'four', 'five'):
                            if numbers_list[j + 1] in ('two', 'three', 'four
