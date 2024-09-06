from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    res = ""
    for c in numbers:
        if c == "zero":
            res += "zero"
        elif c == "one":
            res += "one"
        elif c == "two":
            res += "two"
        elif c == "three":
            res += "three"
        elif c == "four":
            res += "four"
        elif c == "five":
            res += "five"
        elif c == "six":
            res += "six"
        elif c == "seven":
            res += "seven"
        elif c == "eight":
            res += "eight"
        elif c == "nine":
            res += "nine"
    return res

