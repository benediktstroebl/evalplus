from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    intersperse_list = []

    for num in numbers:
        intersperse_list.append(num)
        intersperse_list.append(delimeter)

    intersperse_list.pop()
    return intersperse_list

