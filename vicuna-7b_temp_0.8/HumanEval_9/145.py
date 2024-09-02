from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 1
    max_values = numbers[:]
    current_max = max_values[-1]
    for value in max_values:
        if value > current_max:
            current_max = value
            n = 1
        else:
            n += 1
    return [current_max for _ in range(n)]

