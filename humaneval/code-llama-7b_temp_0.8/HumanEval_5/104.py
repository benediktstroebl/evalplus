from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if numbers == []:
        return []
    interspersed_list: List[int] = []
    for number in numbers[:-1]:
        interspersed_list.append(number)
        interspersed_list.append(delimeter)
    interspersed_list.append(numbers[-1])
    return interspersed_list

