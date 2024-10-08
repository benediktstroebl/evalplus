from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list_so_far: List[int] = []
    current_max: int = 0
    for current_number in numbers:
        current_max = max(current_max, current_number)
        max_list_so_far.append(current_max)
    return max_list_so_far

