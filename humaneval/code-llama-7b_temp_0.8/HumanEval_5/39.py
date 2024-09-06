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

    if len(numbers) == 1:
        return numbers

    nums_len = len(numbers)
    output = []
    for i in range(nums_len - 1):
        output.append(numbers[i])
        output.append(delimeter)
    output.append(numbers[-1])
    return output

