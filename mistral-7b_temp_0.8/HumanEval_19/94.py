from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    numbers_str = numbers.split()
    numbers_list = []
    for num in numbers_str:
        numbers_list.append(numbers_dict[num])

    numbers_list.sort()
    numbers_str = []
    for num in numbers_list:
        numbers_str.append(numbers_dict[str(num)])

    return " ".join(numbers_str)

