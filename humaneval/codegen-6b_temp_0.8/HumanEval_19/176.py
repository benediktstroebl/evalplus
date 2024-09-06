from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # find the index of each number
    index = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
             'seven': '7', 'eight': '8', 'nine': '9'}
    # store all the numbers in a list
    digit_list = []
    for i in numbers.split(' '):
        for j in index:
            if index[j] == i:
                digit_list.append(j)
    # sort the list
    digit_list.sort()
    # rearrange the elements to form the sorted number
    sort_number = ''
    for i in digit_list:
        sort_number += i
    return sort_number

