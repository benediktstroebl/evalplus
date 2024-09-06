from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    new_numbers = []
    for numeral in numbers.split():
        if numeral == 'zero' or numeral == 'one' or numeral == 'two' or numeral == 'three' or numeral == 'four':
            new_numbers.append(numeral)

    for numeral in new_numbers:
        if numeral == 'one':
            new_numbers[new_numbers.index(numeral)] = 'two'
        if numeral == 'two':
            new_numbers[new_numbers.index(numeral)] = 'three'
        if numeral == 'three':
            new_numbers[new_numbers.index(numeral)] = 'four'
        if numeral == 'four':
            new_numbers[new_numbers.index(numeral)] = 'five'
        if numeral == 'five':
            new_numbers[new_numbers.index(numeral)] = 'six'
        if numeral == 'six':
            new_numbers[new_numbers.index(numeral)] = 'seven'
        if numeral == 'seven':
            new_numbers[new_numbers.index(numeral)] = 'eight'
        if numeral == 'eight':
            new_numbers[new_numbers.index(numeral)] = 'nine'
        if numeral == 'nine':
            new_numbers[new_numbers.index(numeral)] = 'zero'

    return " ".join(str(e) for e in new_numbers)

