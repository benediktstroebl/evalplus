from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    def sort_dict(numbers, keys):
        """ helper function to sort dictionary of numbers """
        return sorted(numbers.items(), key=lambda x: keys.index(x[0]))

    def parse_numbers(numbers):
        """ Helper function to parse input string into a list of numbers """
        return [int(x) for x in numbers.split()]

    numbers = parse_numbers(numbers)

    keys = 'zero one two three four five six seven eight nine'.split()
    sorted_dict = sort_dict(numbers, keys)
    return ' '.join(sorted_dict)
