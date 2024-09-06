from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    m = [None] * n
    curr_max = 0

    for i in range(n):
        if i == 0:
            curr_max = numbers[i]
        else:
            curr_max = max(numbers[i], curr_max)
        m[i] = curr_max

    return m

