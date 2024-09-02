from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_value = None
    for value in numbers:
        if max_value is None:
            max_value = value
            result.append(value)
        elif value < max_value:
            result.append(max_value)
        else:
            max_value = value
            result.append(value)
    return result

