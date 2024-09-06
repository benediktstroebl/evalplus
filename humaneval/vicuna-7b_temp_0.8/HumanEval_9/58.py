from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 1
    result = numbers[:]
    while len(result) > n:
        n = len(result) - 1
        result = [max(result[i:i + n]) for i in range(0, len(result), n)]
    return result

