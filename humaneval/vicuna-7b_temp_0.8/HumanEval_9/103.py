from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    moments = [0] * len(numbers)
    rolling_maxes = [numbers[0]]
    for moment, number in zip(moments, numbers):
        rolling_maxes.append(number)
        moments[moment] = max(moments[moment - 1], number)
    return rolling_maxes

