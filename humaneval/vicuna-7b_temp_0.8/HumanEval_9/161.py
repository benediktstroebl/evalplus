from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    result = [0] * (n + 1)
    for i in range(n):
        result[i] = numbers[i]
    for i in range(1, n):
        for j in range(i):
            if result[j] > result[i]:
                result[i], result[j] = result[j], result[i]
    return result[n-1]

