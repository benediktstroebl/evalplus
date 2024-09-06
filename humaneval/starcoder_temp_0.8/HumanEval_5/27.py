from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if len(numbers) <= 1:
        return numbers

    interspersed_list = [numbers[0]]

    for n in numbers[1:-1]:
        interspersed_list.append(delimeter)
        interspersed_list.append(n)

    interspersed_list.append(numbers[-1])

    return interspersed_list

