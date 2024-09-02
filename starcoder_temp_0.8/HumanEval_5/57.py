from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers
    if len(numbers) == 1:
        return numbers

    final_list = []
    for i in range(0, len(numbers) - 1):
        final_list.append(numbers[i])
        final_list.append(delimeter)
    final_list.append(numbers[-1])
    return final_list
