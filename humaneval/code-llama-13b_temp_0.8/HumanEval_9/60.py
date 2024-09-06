from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_value = None
    max_index = -1
    max_list = []

    for index, value in enumerate(numbers):
        if max_value is None or value > max_value:
            max_value = value
            max_index = index

        max_list.append(max_value)

    return max_list

