# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    """
    result = []
    for i in range(len(numbers)):
        if i != 0:
            result.append(delimiter)
        result.append(numbers[i])
    return result
