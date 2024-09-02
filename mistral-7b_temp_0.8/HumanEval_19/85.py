from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numbers_list = numbers.split(' ')
    sorted_numbers = []

    for number in numbers_list:
        if number == "one":
            sorted_numbers.append(0)
        if number == "two":
            sorted_numbers.append(1)
        if number == "three":
            sorted_numbers.append(2)
        if number == "four":
            sorted_numbers.append(3)
        if number == "five":
            sorted_numbers.append(4)
        if number == "six":
            sorted_numbers.append(5)
        if number == "seven":
            sorted_numbers.append(6)
        if number == "eight":
            sorted_numbers.append(7)
        if number == "nine":
            sorted_numbers.append(8)
        if number == "zero":
            sorted_numbers.append(9)

    print(sorted_numbers)

