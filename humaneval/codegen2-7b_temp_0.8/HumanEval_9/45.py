from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maxes = [numbers[0]] * len(numbers)
    maxes[0] = numbers[0]
    for i, n in enumerate(numbers[1:]):
        maxes[i + 1] = max(n, maxes[i])
    return maxes

