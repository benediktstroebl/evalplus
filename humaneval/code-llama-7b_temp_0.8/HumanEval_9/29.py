from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_array = []
    current_max = None
    for element in numbers:
        if current_max is None:
            current_max = element
        if element > current_max:
            current_max = element
        rolling_max_array.append(current_max)

    return rolling_max_array

