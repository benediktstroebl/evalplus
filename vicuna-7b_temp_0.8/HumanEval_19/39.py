from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # regex to match string with numbers from 'zero' to 'nine'
    pattern = r'([0-9]+)'
    # convert string to list of numbers
    numbers_list = [int(match.group(0)) for match in re.finditer(pattern, numbers)]
    # sort numbers
    numbers_list.sort()
    # join sorted numbers to a string
    return ' '.join(str(num) for num in numbers_list)

