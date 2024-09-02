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

    output: List[int] = []

    for i in range(1, len(numbers)):
        output.extend([numbers[i - 1], delimeter])
    output.append(numbers[-1])
    return output

