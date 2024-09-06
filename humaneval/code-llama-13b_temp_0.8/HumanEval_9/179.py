from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_elem = None
    rolling_max_nums = []

    for elem in numbers:
        if rolling_max_elem is None or elem > rolling_max_elem:
            rolling_max_elem = elem

        rolling_max_nums.append(rolling_max_elem)

    return rolling_max_nums

