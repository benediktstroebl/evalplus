from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_roll = [0] * len(numbers)
    for i, num in enumerate(numbers):
        if i == 0:
            max_roll[i] = num
        else:
            max_roll[i] = max(num, max_roll[i - 1])
    return max_roll

