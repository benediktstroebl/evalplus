from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    for idx, n in enumerate(numbers):
        max_n = n
        if idx > 0:
            max_n = max(max_n, result[-1])
        result.append(max_n)
    return result

