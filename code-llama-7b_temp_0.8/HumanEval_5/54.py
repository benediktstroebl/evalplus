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

    interspersed_list = [numbers[0]]
    for i in range(1, len(numbers)):
        interspersed_list.append(delimeter)
        interspersed_list.append(numbers[i])

    return interspersed_list

