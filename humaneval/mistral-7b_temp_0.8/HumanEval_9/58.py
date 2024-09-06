from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maxes = []
    max_so_far = numbers[0]
    for i in range(len(numbers)):
        maxes.append(max_so_far)
        if numbers[i] > max_so_far:
            max_so_far = numbers[i]
    return maxes

