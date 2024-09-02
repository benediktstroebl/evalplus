from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    words = numbers.split()
    numbers = []

    for word in words:
        number = get_number(word)
        numbers.append(number)

    numbers.sort()
    result = ''
    for number in numbers:
        result += number + ' '
    return result

