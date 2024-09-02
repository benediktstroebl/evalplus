from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_till_now, result = float('-inf'), []

    for current in numbers:
        max_till_now = max(current, max_till_now)
        result.append(max_till_now)

    return result

