from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    size = len(numbers)
    rolling_max_nums = [0] * size
    rolling_max_nums[0] = numbers[0]

    for i in range(1, size):
        rolling_max_nums[i] = max(numbers[i], rolling_max_nums[i - 1])

    return rolling_max_nums

