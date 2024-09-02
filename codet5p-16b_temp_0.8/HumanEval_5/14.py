from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    assert isinstance(numbers, list)
    assert isinstance(delimeter, int)
    assert len(numbers) > 0
    assert delimeter >= 0
    result = []
    for i in range(len(numbers)):
        if i!= len(numbers) - 1:
            result += numbers[i], delimeter
        else:
            result += numbers[i]
    return result

