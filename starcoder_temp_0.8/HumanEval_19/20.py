from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # print("input:", numbers)
    # numbers = numbers.split()
    # print("space split:", numbers)
    # numbers = [int(num) for num in numbers]
    # print("converted:", numbers)
    # numbers.sort()
    # print("sorted:", numbers)
    # output = [str(num) for num in numbers]
    # print("output:", output)
    # output = " ".join(output)
    # print("returning:", output)
    # return output
    return " ".join(sorted(numbers.split()))

