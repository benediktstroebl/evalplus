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
    
    new_list = [numbers[0]]
    for idx in range(1, len(numbers)):
        if idx % 2 == 0:
            new_list.append(delimeter)
        new_list.append(numbers[idx])
    return new_list
    
    
