from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a list with values from 0 to 9.
    sort_order = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    # Create a dictionary to look up the value for a number.
    dict_numbers = {}
    for i in range(len(sort_order)):
        dict_numbers[sort_order[i]] = i

    # Convert the input into a list.
    numbers_list = numbers.split()

    # Use the values from the dictionary to sort the list.
    numbers_list.sort(key=lambda x: dict_numbers[x])

    return " ".join(numbers_list)

