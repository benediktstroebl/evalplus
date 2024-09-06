from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    assert len(numbers) > 0
    assert all([x in '0123456789' for x in numbers])
    numbers = numbers.split(' ')
    for i in range(1, len(numbers)):
        place = i
        while place > 0 and numbers[place - 1] > numbers[place]:
            numbers[place], numbers[place - 1] = numbers[place - 1], numbers[place]
            place -= 1
    return ' '.join(numbers)

