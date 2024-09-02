from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers.append(None)  # add a guard element in the end

    i = 0  # start of a sublist with no `delimeter`
    result = []
    while i < len(numbers) - 1:
        result.append(numbers[i])
        i += 1
        result.append(delimeter)
    return result[:-1]  # skip the last `delimeter`

