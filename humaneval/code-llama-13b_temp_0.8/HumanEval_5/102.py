from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    output_list = []
    for i, number in enumerate(numbers):
        output_list.append(number)
        if i < len(numbers) - 1:
            output_list.append(delimeter)

    return output_list

