from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    valid_choices = 'zero one two three four five six seven eight nine'
    numbers = numbers.lower()
    sorted_numbers = []

    for number in numbers:
        if number in valid_choices:
            sorted_numbers.append(number)
        else:
            sorted_numbers.append(valid_choices.index(number))

    return ' '.join(sorted_numbers)

