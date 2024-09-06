from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_nums = []
    current_max = numbers[0]
    rolling_max_nums.append(current_max)
    for num in numbers[1:]:
        current_max = max(current_max, num)
        rolling_max_nums.append(current_max)
    return rolling_max_nums

