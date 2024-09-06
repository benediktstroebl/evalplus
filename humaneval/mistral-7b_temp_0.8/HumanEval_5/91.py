from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    list_len = len(numbers)
    if list_len == 0:
        return []
    if list_len == 1:
        return [numbers[0]]
    list_with_delimeter = [numbers[0]]
    for i in range(1, list_len):
        list_with_delimeter.append(delimeter)
        list_with_delimeter.append(numbers[i])
    return list_with_delimeter

