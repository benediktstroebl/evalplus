from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # first we create a list of numberals
    numbers_list = numbers.split()
    # and we create a list of corresponding integer values
    values_list = [translate_to_value(x) for x in numbers_list]
    # now we can sort the numbers_list
    sorted_list = sorted(values_list)
    # and now we can translate them back to numberals
    result = [translate_to_numberal(x) for x in sorted_list]
    # and finally we join them
    return ' '.join(result)

