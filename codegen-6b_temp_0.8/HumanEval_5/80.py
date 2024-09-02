from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    elif len(numbers) < 2:
        return numbers + [delimeter]

    elif len(numbers) == 2:
        return numbers + [numbers[0], numbers[1], delimeter]

    else:
        return numbers[0:1] + [numbers[0], numbers[1], delimeter] + numbers[2:]

