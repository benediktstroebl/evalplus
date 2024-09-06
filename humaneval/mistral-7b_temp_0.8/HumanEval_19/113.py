from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    sorted_numbers = ""
    i = 0
    for n in numbers.split(" "):
        if n == "one":
            sorted_numbers += "1"
            i += 1
        elif n == "two":
            sorted_numbers += "2"
            i += 1
        elif n == "three":
            sorted_numbers += "3"
            i += 1
        elif n == "four":
            sorted_numbers += "4"
            i += 1
        elif n == "five":
            sorted_numbers += "5"
            i += 1
        elif n == "six":
            sorted_numbers += "6"
            i += 1
        elif n == "seven":
            sorted_numbers += "7"
            i += 1
        elif n == "eight":
            sorted_numbers += "8"
            i += 1
        elif n == "nine":
            sorted_numbers += "9"
            i += 1
        elif n == "zero":
            sorted_numbers
