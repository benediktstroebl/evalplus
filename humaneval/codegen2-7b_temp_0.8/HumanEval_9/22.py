from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_sum = 0
    max_sum_range = []
    for i in range(len(numbers)):
        max_sum = max(max_sum, numbers[i])
        if numbers[i] == max_sum:
            max_sum_range.append(max_sum)
    return max_sum_
