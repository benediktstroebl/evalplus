from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers or delimeter < 0:
        return []
    if len(numbers) == 1:
        return [delimeter]

    return [numbers[0]] + list(interleave(intersperse(numbers[1:], delimeter), n))

