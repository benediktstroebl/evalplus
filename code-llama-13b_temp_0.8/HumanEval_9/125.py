from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_val = numbers[0]
    result: List[int] = []

    for number in numbers:
        rolling_max_val = max(rolling_max_val, number)
        result.append(rolling_max_val)

    return result

