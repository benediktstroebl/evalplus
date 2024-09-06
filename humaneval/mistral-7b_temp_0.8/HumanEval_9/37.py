from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    i = 1
    maxes = [numbers[0]]
    for number in numbers[1:]:
        maxes.append(max(maxes[-i:] + [number], default=number))
        i += 1
    return maxes

