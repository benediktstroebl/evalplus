from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) > 0:
        interspersed = [numbers[0]]
        for next in numbers[1:]:
            interspersed.append(delimeter)
            interspersed.append(next)
        return interspersed
    return
