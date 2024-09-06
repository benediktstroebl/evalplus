from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    i, j = 0, 1
    while j < len(numbers):
        if numbers[j] > numbers[i]:
            result.append(numbers[j])
            i = j
        j += 1
    return result

