from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 0
    window = numbers[:]
    while n < len(numbers):
        window.remove(numbers[n])
        n += 1
        max_val = max(window)
        window.append(max_val)
    return window[::-1]

