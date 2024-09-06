from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = []
    rolling_max_value: int = 0

    for number in numbers:
        rolling_max_value = max(rolling_max_value, number)
        result.append(rolling_max_value)

    return result

