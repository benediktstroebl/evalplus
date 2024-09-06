from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max = []
    window_start = 0
    rolling_max.append(numbers[window_start])
    for window_end in range(1, len(numbers)):
        if numbers[window_end] >= rolling_max[window_start]:
            rolling_max.append(numbers[window_end])
            window_start += 1
        else:
            rolling_max.append(rolling_max[window_start])
    return rolling_max

