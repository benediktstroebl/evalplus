from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    return list(map(lambda _n: delimeter if _n!= numbers[len(numbers) - 1] else numbers[len(numbers) - 1], numbers))
    # return list(map(lambda _n: delimeter if _n!= numbers[len(numbers) - 1] else numbers[len(numbers) - 1], numbers))
    # return [delimeter if _n!= numbers[len(numbers) - 1] else numbers[len(numbers) - 1] for _n in numbers]
    # return [delimeter if _n!= numbers[len(numbers) - 1] else numbers[len(numbers) - 1] for _n in numbers]

