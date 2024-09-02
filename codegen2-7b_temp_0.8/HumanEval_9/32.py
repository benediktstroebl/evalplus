from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    start_idx = 1
    end_idx = start_idx
    max_num = numbers[0]
    while end_idx < len(numbers):
        cur_num = numbers[end_idx]
        if cur_num > max_num:
            max_num = cur_num
        end_idx += 1
    return [max_num]
