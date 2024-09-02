from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maxes = [0] * len(numbers)

    for i, n in enumerate(numbers):
        maxes[i] = max(maxes[i - 1] + 1, n)

    return
