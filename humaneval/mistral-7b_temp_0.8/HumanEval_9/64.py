from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_start_index = 0
    rolling_maxes = []
    for i in range(1, len(numbers)):
        if numbers[i - 1] < numbers[i]:
            max_start_index = i
            rolling_maxes.append(numbers[i])
        else:
            rolling_maxes.append(numbers[max_start_index])
    return rolling_maxes

