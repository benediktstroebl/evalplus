from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    small = numbers[0]
    large = numbers[-1]
    if small == large:
        return (small, large)
    if numbers[1] - small < large - numbers[-2]:
        return (small, numbers[1])
    return (small, large)


import pytest
from sortedcontainers import SortedList

