from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []
    for i in range(len(numbers) * 2):
        if i % 2 != 0:
            result.append(delimeter)
        try:
            result.append(numbers[i // 2])
        except IndexError:
            break

    return result

