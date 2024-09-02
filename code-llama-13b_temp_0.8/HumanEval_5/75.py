from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # return sum([[i, delimeter] for i in numbers[:-1]], [numbers[-1]])[0] if numbers else []
    # return sum(zip(numbers, [delimeter] * (len(numbers) - 1)), [])
    return [x for t in zip(numbers, [delimeter] * (len(numbers) - 1)) for x in t] + [numbers[-1]] if numbers else []

