from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = -1
    max_index = -1
    result = []
    for i, num in enumerate(numbers):
        result.append(max_num)
        if num > max_num:
            max_num = num
            max_index = i
    result[max_index] = max_num
    return result

