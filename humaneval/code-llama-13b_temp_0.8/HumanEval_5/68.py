from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    interspersed_numbers = []
    interspersed_numbers.append(numbers[0])
    for number in numbers[1:]:
        interspersed_numbers.append(delimeter)
        interspersed_numbers.append(number)
    return interspersed_numbers

