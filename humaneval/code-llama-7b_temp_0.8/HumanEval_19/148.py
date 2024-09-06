from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split into a list of strings
    num_list = numbers.split(" ")

    # iterate over list
    for i, num in enumerate(num_list):
        # convert string to int
        try:
            num_list[i] = int(num)
        except ValueError:
            continue

    # sort
    num_list.sort()

    # convert ints back to strings
    for i, num in enumerate(num_list):
        num_list[i] = str(num)

    # join the list into a string
    return " ".join(num_list)

