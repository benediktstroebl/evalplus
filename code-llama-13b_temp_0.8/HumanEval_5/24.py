from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # if len(numbers) == 0:
    #     return []
    # temp = [numbers[0]]
    # for i in range(1, len(numbers)):
    #     if i % 2 == 1:
    #         temp.append(delimeter)
    #     temp.append(numbers[i])
    # return temp
    return numbers[::2] + [delimeter] * (len(numbers) - 1) + numbers[1::2] if len(numbers) else []

