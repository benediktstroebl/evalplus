from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # This function does the same thing as the one you wrote in the previous exercise,
    # but it doesn't rely on the "for" loop construct. It relies on the built-in function
    # "enumerate()" and the special "in" operator. It is recommended that you also write this
    # function without relying on any built-in function.
    if not numbers:
        return []
    if len(numbers) == 1:
        return numbers + [delimeter]
    return [numbers[i] for i, n in enumerate(numbers) if i % 2 == 0] + [
        delimeter
    ] + [n for i, n in enumerate(numbers) if i % 2 == 1]

