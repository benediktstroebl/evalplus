from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    split_numbers = numbers.split(" ")
    for i in range(len(split_numbers)):
        for j in range(i+1, len(split_numbers)):
            if int(split_numbers[i]) > int(split_numbers[j]):
                split_numbers[i], split_numbers[j] = split_numbers[j], split_numbers[i]
    return " ".join(split_numbers)

