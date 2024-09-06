from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # My first solution
    # return numbers[::2] + [delimeter] + numbers[1::2]

    # 2nd solution
    # return [delimeter] + [x for i in range(len(numbers)) for x in [numbers[i], delimeter] if i < len(numbers)]

    # 3rd solution
    result = []
    for i, _ in enumerate(numbers):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

