from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    words = numbers.split()
    int_list = []
    for word in words:
        if word == 'zero':
            int_list.append(0)
        elif word == 'one':
            int_list.append(1)
        elif word == 'two':
            int_list.append(2)
        elif word == 'three':
            int_list.append(3)
        elif word == 'four':
            int_list.append(4)
        elif word == 'five':
            int_list.append(5)
        elif word == 'six':
            int_list.append(6)
        elif word == 'seven':
            int_list.append(7)
        elif word == 'eight':
            int_list.append(8)
        elif word == 'nine':
            int_list.append(9)
        else:
            raise ValueError(f'Invalid number: {word}')

    int_list.sort()
    return ' '.join(str(number) for number in int_list)

