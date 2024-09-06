from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # create list of numberals and numbers from the string
    numberals_list = numbers.split()
    # create list of the numbers
    numberals_list = [numberals_list.index(number) for number in numberals_list]
    # create list of the numberals
    numberals_list = [numberals_list.index(number) for number in numberals_list]
    # sort the numbers
    numberals_list.sort()
    # create list of the numberals
    numberals_list = [numberals_list[number] for number in numberals_list]
    # create string from numberals
    numberals = ' '.join(numberals_list)
    return numberals

