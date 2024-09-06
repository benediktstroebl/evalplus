from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_value = None
    max_result = []

    for number in numbers:
        if max_value is None or number > max_value:
            max_value = number
        max_result.append(max_value)

    return max_result

