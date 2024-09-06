from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_array: List[int] = []
    rolling_max_element: int = 0
    for i, element in enumerate(numbers):
        rolling_max_element = max(rolling_max_element, element)
        rolling_max_array.append(rolling_max_element)
    return rolling_max_array

