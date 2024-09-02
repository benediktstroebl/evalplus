from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    array_of_numbers = numbers.split()
    for i in range(len(array_of_numbers)):
        if array_of_numbers[i] == 'one':
            array_of_numbers[i] = '0'
        elif array_of_numbers[i] == 'two':
            array_of_numbers[i] = '1'
        elif array_of_numbers[i] == 'three':
            array_of_numbers[i] = '2'
        elif array_of_numbers[i] == 'four':
            array_of_numbers[i] = '3'
        elif array_of_numbers[i] == 'five':
            array_of_numbers[i] = '4'
        elif array_of_numbers[i] == 'six':
            array_of_numbers[i] = '5'
        elif array_of_numbers[i] == 'seven':
            array_of_numbers[i] = '6'
        elif array_of_numbers[i] == 'eight':
            array_of_numbers[i] = '7'
        elif array_of_numbers[i] == 'nine':
            array_of_numbers[i] = '8'
    return ' '.join(array_of_numbers)

