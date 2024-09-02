from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # if empty list, return empty list
    if not numbers:
        return []
    # else, start with the first element of `numbers' and insert a `delimeter' between every two consecutive elements
    else:
        intersperse_list = [numbers[0]]
        for i in range(1, len(numbers)):
            intersperse_list.append(delimeter)
            intersperse_list.append(numbers[i])
        return intersperse_list

