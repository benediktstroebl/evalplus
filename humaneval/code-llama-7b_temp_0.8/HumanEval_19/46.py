from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if len(numbers.split()) == 0:
        return ''
    if numbers.split() == ['one']:
        return 'one'
    new_list = []
    for i in numbers.split():
        if i == 'zero':
            new_list.append(0)
        if i == 'one':
            new_list.append(1)
        if i == 'two':
            new_list.append(2)
        if i == 'three':
            new_list.append(3)
        if i == 'four':
            new_list.append(4)
        if i == 'five':
            new_list.append(5)
        if i == 'six':
            new_list.append(6)
        if i == 'seven':
            new_list.append(7)
        if i == 'eight':
            new_list.append(8)
        if i == 'nine':
            new_list.append(9)
    new_list.sort()
    result = ''
    for i in new_list:
        if i == 0:
            result += 'zero '
        if i == 1:
            result += 'one '
        if i == 2:
            result += 'two '
        if i == 3:
            result += 'three '
        if i == 4:
            result += 'four '
        if i == 5:
            result += 'five '
        if i == 6:
            result += 'six '
        if i == 7:
            result += 'seven '
        if i == 8:
            result += 'eight '
        if i == 9:
            result += 'nine '
    return result[:-1]

