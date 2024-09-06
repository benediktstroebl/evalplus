from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = [0] * len(numbers)
    max_value = 0
    for i in range(len(numbers)):
        if max_value < numbers[i]:
            max_value = numbers[i]
        rolling_max[i] = max_value
    return rolling_
