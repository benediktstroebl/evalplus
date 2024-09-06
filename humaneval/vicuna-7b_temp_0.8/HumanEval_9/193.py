from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = []
    current_max = None
    for num in numbers:
        if current_max is not None and num > current_max:
            rolling_max.append(current_max)
            current_max = num
        else:
            current_max = num
    rolling_max.append(current_max)
    return rolling_max

