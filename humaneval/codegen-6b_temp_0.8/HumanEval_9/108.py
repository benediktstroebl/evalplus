from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = max(numbers)
    result = [max_val]
    for i, val in enumerate(numbers):
        max_val = max(val, max_val)
        if val < max_val:
            result.append(max_val)
    return result

