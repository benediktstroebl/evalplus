from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    max_value = None
    for element in numbers:
        if max_value is None:
            max_value = element
        else:
            max_value = max(max_value, element)
        result.append(max_value)
    return result

