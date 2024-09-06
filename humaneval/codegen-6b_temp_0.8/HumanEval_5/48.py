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
    i = 0
    res = [numbers[0]]
    while True:
        if i + 1 >= len(numbers):
            res.append(numbers[i])
            break
        if numbers[i] != delimeter:
            res.append(numbers[i])
        if numbers[i + 1] != delimeter:
            res.append(delimeter)
        i += 1
    return res

