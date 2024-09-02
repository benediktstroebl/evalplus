from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    output_list = []
    if len(numbers) > 0:
        output_list.append(numbers[0])
    for i in range(1, len(numbers)):
        if i == len(numbers) - 1:
            output_list.append(numbers[i])
        else:
            output_list.append(numbers[i])
            output_list.append(delimeter)
    return output_list

