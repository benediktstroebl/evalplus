from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_max = -1
    rolling_max = []
    for i in numbers:
        if i > previous_max:
            previous_max = i
        rolling_max.append(previous_max)
    return rolling_max

