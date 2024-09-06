from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    numbers.append(delimeter)
    numbers.append(delimeter)

    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] == delimeter:
            numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]

    del numbers[-1]
    del numbers[-1]
    return numbers

