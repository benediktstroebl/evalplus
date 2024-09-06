from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    rolling_max = [None] * n
    for i in range(1, n):
        for j in range(i, n):
            if numbers[j] > rolling_max[i]:
                rolling_max[i] = numbers[j]
    return rolling_max

