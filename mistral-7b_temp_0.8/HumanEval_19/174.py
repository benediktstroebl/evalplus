from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    s = numbers.split()
    for i in range(len(s)):
        for j in range(len(s)):
            if int(s[i]) > int(s[j]):
                s[i], s[j] = s[j], s[i]
    return " ".join(s)

