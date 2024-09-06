from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    i = 0
    length = len(numbers)
    p = len(numbers) // 2
    output = []
    while i < length - 1:
        output.append(numbers[i])
        output.append(delimeter)
        output.append(numbers[i + 1])
        i += 1
    if length % 2 != 0:
        output.append(numbers[length - 1])
    return output

