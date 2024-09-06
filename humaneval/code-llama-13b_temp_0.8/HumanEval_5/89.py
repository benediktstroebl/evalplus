from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if not numbers:
        return numbers

    delimetered_list: List[int] = []

    delimetered_list.append(numbers[0])

    for number in numbers[1:]:
        delimetered_list += [delimeter, number]

    return delimetered_list

