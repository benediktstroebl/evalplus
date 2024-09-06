from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if delimeter <= 0:
        raise ValueError("Delimeter cannot be a negative number")
    elif len(numbers) < 2:
        return numbers
    else:
        numbers.insert(0, delimeter)
        numbers.extend(numbers[-2::-2])
        return numbers

