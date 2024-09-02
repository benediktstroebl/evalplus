from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_at_index = [None] * len(numbers)
    max_at_index[0] = numbers[0]
    for i in range(1, len(numbers)):
        max_at_index[i] = max(max_at_index[i - 1], numbers[i])
    return max_at_index

