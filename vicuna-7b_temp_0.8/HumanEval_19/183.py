from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    #convert string to list of integers
    numbers = [int(n) for n in numbers.split()]

    #sort the list in ascending order
    numbers.sort()

    #reverse the list so the smallest number is first
    numbers.reverse()

    #convert the sorted list to a string
    return ' '.join(map(str, numbers))

