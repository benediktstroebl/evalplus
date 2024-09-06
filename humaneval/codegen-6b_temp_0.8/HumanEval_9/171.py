from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    for idx, num in enumerate(numbers):
        length = len(numbers) - idx
        if length == 0:
            max_list.append(num)
            continue
        if max_list and num > max_list[-1]:
            max_list.append(num)
        else:
            max_list.append(max_list[-1])
    return max_list

