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
        if word in _number_dict:
            numbers.append(_number_dict[word])

    numbers.sort()
    result = []
    for number in numbers:
        for word in _number_dict:
            if _number_dict[word] == number:
                result.append(word)
    return ' '.join(result)


    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9

