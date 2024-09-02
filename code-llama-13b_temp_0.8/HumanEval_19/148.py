from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    my_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    numbers_list: List = numbers.split()
    nums_list: List = []
    for number in numbers_list:
        nums_list.append(my_dict[number])
    nums_list.sort()
    sorted_numbers: str = ""
    for number in nums_list:
        sorted_numbers += list(my_dict.keys())[list(my_dict.values()).index(number)] + " "
    return sorted_numbers[:-1]

