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

    intersperse.accumulator = []

    def helper(list_: List[int], delimeter: int):
        if list_:
            intersperse.accumulator.append(list_[0])
            helper(list_[1:], delimeter)
        if list_:
            intersperse.accumulator.append(delimeter)

    helper(numbers, delimeter)
    return intersperse.accumulator

