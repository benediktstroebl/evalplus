from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # if len(numbers) < 2:
    #     return numbers
    # else:
    #     return numbers[0:1] + [delimeter] + intersperse(numbers[1:], delimeter)
    # # return numbers[:-1] + [delimeter] + numbers[-1:]
    # return numbers
    # new = numbers[:-1]
    # new.extend([delimeter, numbers[-1]])
    # return new
    new = []
    for i in range(len(numbers)):
        new.append(numbers[i])
        if i != len(numbers) - 1:
            new.append(delimeter)
    return new

