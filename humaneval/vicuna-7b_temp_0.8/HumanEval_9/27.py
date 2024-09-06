from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = max(numbers)
    rolling_max_list = [max_val]
    current_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] >= max_val:
            max_val = numbers[i]
        rolling_max_list[current_index] = max_val
        current_index += 1
    return rolling_max_list