from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    list_of_words = numbers.split(' ')
    sorted_list = []

    for word in list_of_words:
        if word == 'zero':
            sorted_list.append(0)
        elif word == 'one':
            sorted_list.append(1)
        elif word == 'two':
            sorted_list.append(2)
        elif word == 'three':
            sorted_list.append(3)
        elif word == 'four':
            sorted_list.append(4)
        elif word == 'five':
            sorted_list.append(5)
        elif word == 'six':
            sorted_list.append(6)
        elif word == 'seven':
            sorted_list.append(7)
        elif word == 'eight':
            sorted_list.append(8)
        else:
            sorted_list.append(9)

    sorted_list.sort()
    sorted_string = ''

    for i in sorted_list:
        if i == 0:
            sorted_string += 'zero '
        elif i == 1:
            sorted_string += 'one '
        elif i == 2:
            sorted_string += 'two '
        elif i == 3:
            sorted_string += 'three '
        elif i == 4:
            sorted_string += 'four '
        elif i == 5:
            sorted_string += 'five '
        elif i == 6:
            sorted_string += 'six '
        elif i == 7:
            sorted_string += 'seven '
        elif i == 8:
            sorted_string += 'eight '
        else:
            sorted_string += 'nine '

    return sorted_string[:-1]

