from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    types = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    new_numbers = []
    for word in numbers.split():
        try:
            new_numbers.append(types[word])
        except KeyError:
            value = int(word)
            if value < 0:
                new_numbers.append(abs(value))
            else:
                new_numbers.append(value)
    return ' '.join(str(num) for num in sorted(new_numbers))

