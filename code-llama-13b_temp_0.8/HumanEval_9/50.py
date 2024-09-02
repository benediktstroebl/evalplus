from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = -float("inf")
    max_list = []
    for number in numbers:
        if current_max < number:
            current_max = number
        max_list.append(current_max)
    return max_list

