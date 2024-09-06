from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # This is a functional solution, which is also the more efficient one.
    # if len(numbers) < 2:
    #     return numbers
    # return [numbers[0]] + [delimeter] + intersperse(numbers[1:], delimeter)

    # This is a non-functional solution, which is also the less efficient one.
    for i in range(len(numbers) - 1, -1, -1):
        numbers.insert(2 * i, delimeter)
    return numbers

