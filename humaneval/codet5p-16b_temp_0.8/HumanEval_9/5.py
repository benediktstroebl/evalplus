from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    out: List[int] = []
    i = 0
    while i < len(numbers):
        max_n = max(numbers[i:])
        out.append(max_n)
        i += 1
    return out
