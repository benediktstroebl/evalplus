from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [0] * len(numbers)
    current_max = 0
    for i in range(len(numbers)):
        current_max = max(numbers[i], current_max)
        result[i] = current_max
    return result

