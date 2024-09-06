from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split(' ')

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] == 'zero':
                numbers[i] = '0'
            elif numbers[i] == 'one':
                numbers[i] = '1'
            elif numbers[i] == 'two':
                numbers[i] = '2'
            elif numbers[i] == 'three':
                numbers[i] = '3'
            elif numbers[i] == 'four':
                numbers[i] = '4'
            elif numbers[i] == 'five':
                numbers[i] = '5'
            elif numbers[i] == 'six':
                numbers[i] = '6'
            elif numbers[i] == 'seven':
                numbers[i] = '7'
            elif numbers[i] == 'eight':
                numbers[i] = '8'
            elif numbers[i] == 'nine':
                numbers[i] = '9'

            if numbers[j] == 'zero':
                numbers[j] = '0'
            elif numbers[j] == 'one':
                numbers[j] = '1'
            elif numbers[j] == 'two':
                numbers[j] = '2'
            elif numbers[j] == 'three':
                numbers[j] = '3'
            elif numbers[j] == 'four':
                numbers[j] = '4'
            elif numbers[j] == 'five':
                numbers[j] = '5'
            elif numbers[j] == 'six':
                numbers[j] = '6'
            elif numbers[j] == 'seven':
                numbers[j] = '7'
            elif numbers[j] == 'eight':
                numbers[j] = '8'
            elif numbers[j] == 'nine':
                numbers[j] = '9'

            if int(numbers[i]) > int(numbers[j]):
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return ' '.join(numbers)

