from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maxes = []

    for i, num in enumerate(numbers[:-1]):
        maxes.append(max(numbers[i + 1 :]) if num < numbers[i + 1] else num)

    return maxes

