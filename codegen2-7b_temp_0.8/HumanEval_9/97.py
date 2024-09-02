from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = -1
    max_list = [0] * len(numbers)
    for i, _ in enumerate(numbers):
        max_val = max(max_val, numbers[i])
        max_list[i] = max_val
    return max_list

