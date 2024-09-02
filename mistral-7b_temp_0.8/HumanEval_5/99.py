from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    answer = [numbers[0]]
    for i in range(len(numbers)):
        if i == len(numbers)-1:
            answer.append(numbers[i])
        else:
            answer.append(delimeter)
            answer.append(numbers[i])
    return answer

