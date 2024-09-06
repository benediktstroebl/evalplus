from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # "..(x)y.." => "(x)y(x)"
    # "[1, 2, 3, 4, 5]" =>
    # => "[1, 4, 2, 4, 3, 4, 5]"
    # => "[1, 4, 2, 4, 3, 4, 5, 4]"
    # => "[1, 4, 2, 4, 3, 4, 5, 4, 5]"
    # => "[1, 4, 2, 4, 3, 4, 5, 4, 5, 4]"
    # => "[1, 4, 2, 4, 3, 4, 5, 4, 5, 4, 5]"
    # => "1, 4, 2, 4, 3, 4, 5, 4, 5, 4, 5"
    return [n for sublist in list(zip(numbers, [delimeter] * (len(numbers) + 1))) for n in sublist][:-1]

