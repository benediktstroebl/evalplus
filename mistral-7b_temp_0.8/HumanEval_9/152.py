from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_values: List[int] = []
    max_value = None
    for number in numbers:
        if max_value is None or max_value < number:
            max_value = number
        max_values.append(max_value)
    return max_values

