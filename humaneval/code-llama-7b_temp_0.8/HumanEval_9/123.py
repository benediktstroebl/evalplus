from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) < 2:
        return numbers
    max_val = 0
    max_list: List[int] = []
    for index, value in enumerate(numbers):
        if index == 0:
            max_val = value
        if value > max_val:
            max_val = value
        max_list.append(max_val)
    return max_list

