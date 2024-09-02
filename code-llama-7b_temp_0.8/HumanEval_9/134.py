from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_nums = [0] * len(numbers)
    for i, _ in enumerate(numbers):
        if i == 0:
            max_nums[i] = numbers[i]
        else:
            max_nums[i] = max(numbers[i], max_nums[i - 1])
    return max_nums

