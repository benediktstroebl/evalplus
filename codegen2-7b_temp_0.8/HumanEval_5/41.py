from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    assert delimeter!= 0
    assert numbers!= []
    l = len(numbers)
    i = 0
    while i < l - 1:
        numbers.insert(i + 1, delimeter)
        i += 1
    
