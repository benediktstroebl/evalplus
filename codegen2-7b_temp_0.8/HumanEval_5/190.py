from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    previous_number = numbers[0]
    new_list = []
    for number in numbers[1:]:
        new_list.append(previous_number)
        previous_number = number
    new_list.append(previous_number)

    return new_
