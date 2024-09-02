from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maxes = []
    for n in numbers:
        if len(maxes) == 0:
            maxes.append(n)
        elif n > maxes[-1]:
            maxes.append(n)
        else:
            maxes.append(maxes[-1])
    return maxes

