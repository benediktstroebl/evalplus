from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    maxes = []
    for i, n in enumerate(numbers):
        if n > max_so_far:
            max_so_far = n
            maxes.clear()
            maxes.append(n)
        elif n == max_so_far:
            maxes.append(n)
    return
