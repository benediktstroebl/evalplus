from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_v = numbers[0]
    max_n = 1
    for n in range(1, len(numbers)):
        if numbers[n] > max_v:
            max_v = numbers[n]
            max_n = n + 1
    return numbers[:max_n
