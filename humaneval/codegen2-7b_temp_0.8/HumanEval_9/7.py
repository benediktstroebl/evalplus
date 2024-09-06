from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    curr_max: int = 0
    for i, n in enumerate(numbers):
        if n > curr_max:
            curr_max = n
        elif curr_max < n:
            curr_max = n
    return [curr_max] + [max(numbers[i:i + n]) for i, n in enumerate(range(1, len(numbers)), 1)]
