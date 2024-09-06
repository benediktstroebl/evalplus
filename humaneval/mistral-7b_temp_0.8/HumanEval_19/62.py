from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # TODO
    arr = []
    numbers = numbers.split(' ')
    for word in numbers:
        if word == 'zero':
            arr.append(0)
        elif word == 'one':
            arr.append(1)
        elif word == 'two':
            arr.append(2)
        elif word == 'three':
            arr.append(3)
        elif word == 'four':
            arr.append(4)
        elif word == 'five':
            arr.append(5)
        elif word == 'six':
            arr.append(6)
        elif word == 'seven':
            arr.append(7)
        elif word == 'eight':
            arr.append(8)
        elif word == 'nine':
            arr.append(9)
        else:
            raise ValueError(f"'{word}' is not a valid number")
    return ' '.join([str(x) for x in sorted(arr)])

