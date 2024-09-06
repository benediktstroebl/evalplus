from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    intersperse_numbers = []
    # insert numbers into intersperse_numbers
    # intersperse_numbers.extend([delimeter])
    # intersperse_numbers.extend([1, 2, 3])
    for number in numbers:
        intersperse_numbers.extend([number, delimeter])
    return intersperse_numbers[:-1]

