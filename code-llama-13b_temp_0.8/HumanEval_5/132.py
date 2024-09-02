from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if numbers == []:
        return []

    output = []

    for i in range(len(numbers) - 1):
        output.append(numbers[i])
        output.append(delimeter)

    # don't forget the last number
    output.append(numbers[-1])
    return output

