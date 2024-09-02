from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # find and sort numbers from 0 to 9
    # convert str to list
    # split elements in list
    # find index of elements in list
    # sort number using index
    # add numbers in list to new str
    # convert numbers to str
    # return new str
    new_str = ""
    numbers = numbers.split()
    for num in numbers:
        for i, n in enumerate(list("zero one two three four five six seven eight nine".split())):
            if num == n:
                new_str += f" {i}"
    return " ".join(sorted(new_str.split()))

