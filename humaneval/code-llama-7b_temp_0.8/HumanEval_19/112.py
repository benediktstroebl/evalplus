from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if numbers == "":
        return ""
    numbers = numbers.split()
    sorted_nums = []
    for _ in numbers:
        if _ == "zero":
            sorted_nums.append(0)
        elif _ == "one":
            sorted_nums.append(1)
        elif _ == "two":
            sorted_nums.append(2)
        elif _ == "three":
            sorted_nums.append(3)
        elif _ == "four":
            sorted_nums.append(4)
        elif _ == "five":
            sorted_nums.append(5)
        elif _ == "six":
            sorted_nums.append(6)
        elif _ == "seven":
            sorted_nums.append(7)
        elif _ == "eight":
            sorted_nums.append(8)
        elif _ == "nine":
            sorted_nums.append(9)
        else:
            return "invalid input"
    return " ".join([str(_) for _ in sorted(sorted_nums)])

