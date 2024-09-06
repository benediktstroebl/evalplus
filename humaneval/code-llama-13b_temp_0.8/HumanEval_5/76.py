from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # Get the numbers after the first number
    numbers_after_first = numbers[1:]

    # Make a list of all the delimeters we need
    delimeters = [delimeter] * (len(numbers) - 1)

    # Add the numbers and delimeters together
    return [numbers[0]] + [x for pair in zip(delimeters, numbers_after_first) for x in pair]

