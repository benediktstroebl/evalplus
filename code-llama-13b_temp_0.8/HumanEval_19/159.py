from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    list_numbers = []
    list_number_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # extract the numbers and add them to list
    for number in numbers.split(" "):
        list_numbers.append(list_number_map[number])

    # sort the list
    list_numbers.sort()

    # map back to original strings
    list_numbers = [
        list(list_number_map.keys())[list(list_number_map.values()).index(i)]
        for i in list_numbers
    ]

    return " ".join(list_numbers)

