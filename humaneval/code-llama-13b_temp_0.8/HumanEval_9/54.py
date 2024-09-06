from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max = 0
    max_index = 0
    rolling_max = []
    for i, element in enumerate(numbers):
        if element >= max:
            max = element
            max_index = i
        rolling_max.append(max)
    return rolling_max

