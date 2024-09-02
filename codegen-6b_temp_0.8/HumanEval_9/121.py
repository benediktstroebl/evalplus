from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [0] * len(numbers)
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        if number > result[index - 1]:
            result[index] = number
    return result

