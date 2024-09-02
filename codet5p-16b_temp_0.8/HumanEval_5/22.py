from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []
    numbers.insert(0, delimeter)
    numbers.append(delimeter)
    index = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            continue
        else:
            result.append(numbers[index])
            index += 1
    return result
    
