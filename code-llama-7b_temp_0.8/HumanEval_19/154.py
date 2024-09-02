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
        for j in range(len(numbers)):
            if numbers[i] == 'zero' or numbers[i] == 'one' or numbers[i] == 'two':
                if numbers[j] == 'three' or numbers[j] == 'four' or numbers[j] == 'five':
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            elif numbers[i] == 'three':
                if numbers[j] == 'six' or numbers[j] == 'seven' or numbers[j] == 'eight' or numbers[j] == 'nine':
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            elif numbers[i] == 'six':
                if numbers[j] == 'nine':
                    numbers[i], numbers[j] = numbers[j], numbers[i]

    return ' '.join(numbers)

