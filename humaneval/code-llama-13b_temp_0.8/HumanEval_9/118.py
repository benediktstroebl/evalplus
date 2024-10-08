from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_so_far = 0
    rolling_max_nums = []
    for i in range(len(numbers)):
        rolling_max_nums.append(max_so_far)
        max_so_far = max(max_so_far, numbers[i])
    return rolling_max_nums

