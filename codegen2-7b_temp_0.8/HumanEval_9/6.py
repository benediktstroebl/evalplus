from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_until_i = 0
    max_until_j = 0
    max_value = 0

    for i, j in enumerate(numbers):
        if j >= max_value:
            max_until_i = i
            max_until_j = i
            max_value = j
        else:
            if j > max_value:
                max_until_j = i

    return numbers[max_until_i : max_until_
