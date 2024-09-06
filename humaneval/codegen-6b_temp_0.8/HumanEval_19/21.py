from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Another way would be to just split the string on spaces and then sort that, but that would add a sort function and be
    # more complicated:
    # new_string = sorted([int(x) for x in numbers.split()])
    # return ' '.join(str(x) for x in new_string)

    # Another way would be to use a dict (python's implementation is O(n)):
    # count = {x: numbers.count(x) for x in numbers}
    # return ' '.join(map(str, sorted(count.keys(), key=lambda x: count[x])))

    # With this method, the same time complexity remains, but space complexity is O(n):
    # return ' '.join(sorted([int(x) for x in numbers.split()], key=int))

    # Another way would be to first convert to a list, sort the list, and then convert back to a string (in-place):
    # numbers_list = list(numbers.split())
    # sorted_str = sorted(numbers_list, reverse=True)
    # return ''.join(str(x) for x in sorted_str)
    numbers_list = [int(i) for i in numbers.split()]
    return ' '.join(str(i) for i in sorted(numbers_list, reverse=True))

