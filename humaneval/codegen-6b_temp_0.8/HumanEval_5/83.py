from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    inp = {'delimeter': delimeter, 'numbers': numbers}
    result = []
    for i in range(0, len(numbers)):
        if i == 0:
            result.append(numbers[i])
        elif i != 0:
            result.append(numbers[i])
            result.append(delimeter)
    del inp['numbers']
    return result

