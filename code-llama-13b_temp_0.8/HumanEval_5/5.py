from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers_copy = numbers.copy()
    numbers_copy.append(delimeter)
    output = []

    for i in range(len(numbers_copy)):
        if numbers_copy[i] == delimeter:
            if i == len(numbers_copy) - 1:
                break
            output.append(numbers_copy[i])
            output.append(numbers_copy[i + 1])
            del numbers_copy[i]
            del numbers_copy[i]
    return output

