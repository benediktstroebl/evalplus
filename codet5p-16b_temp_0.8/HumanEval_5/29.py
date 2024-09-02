from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    try:
        len_numbers = len(numbers)
        if len_numbers == 0:
            return []
        else:
            return [delimeter] + numbers + [delimeter]
    except TypeError:
        return []
        
