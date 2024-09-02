from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # To store the input in a list
    num_list = numbers.split(" ")
    # To store the sorted numbers in a list
    num_list_sort = []
    for i in range(len(num_list)):
        num_list_sort.append(int(num_list[i]))
    num_list_sort.sort()
    for i in range(len(num_list_sort)):
        num_list[i] = str(num_list_sort[i])
    return " ".join(num_list)

