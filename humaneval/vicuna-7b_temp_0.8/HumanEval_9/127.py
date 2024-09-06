from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    if n == 0:
        return []
    k = 0
    result = numbers[:]
    for i in range(n-1, -1, -1):
        result.remove(numbers[i])
        if result and result[-1] > result[-2]:
            result.remove(result[-1])
        for j in range(i, n):
            result.append(numbers[j])
    return result
