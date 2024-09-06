from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    interspersed_list: List[int] = []
    for x in numbers:
        interspersed_list.append(x)
        interspersed_list.append(delimeter)
    if len(interspersed_list) > 0:
        interspersed_list.pop()  # remove trailing delimeter
    return interspersed_list

