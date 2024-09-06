from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 3
    rolling_max_list = []
    for i in range(len(numbers) - window_size):
        max_number = max(numbers[i: i + window_size])
        rolling_max_list.append(max_number)
    return rolling_max_list

