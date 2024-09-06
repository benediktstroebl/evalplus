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
    result = []
    for i in range(0, len(numbers), 2):
        if len(numbers) - i == 1:
            result.append(numbers[i])
            result.append(delimeter)
            result.append(numbers[i + 1])
            break
        result.append(numbers[i])
        result.append(delimeter)
    return result + intersperse(numbers[(len(numbers) // 2) + 1:], delimeter)

