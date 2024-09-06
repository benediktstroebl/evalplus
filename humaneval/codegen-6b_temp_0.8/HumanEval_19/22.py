from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Use map() to create a list of tuples of (number, index)
    number_index_list = list(zip(numbers, range(len(numbers))))
    number_index_list.sort(key=lambda tup: tup[0])

    # Use list comprehension to create a new list of sorted numbers
    new_list = [number_index_list[i][1] for i in range(len(number_index_list))]

    return ' '.join(new_list)

