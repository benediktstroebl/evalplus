from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_diff = float('inf')
    min_diff_first = 0
    min_diff_second = 0
    for idx, first in enumerate(numbers):
        for jdx, second in enumerate(numbers[idx+1:]):
            diff = abs(first - second)
            if diff < min_diff:
                min_diff = diff
                min_diff_first = first
                min_diff_second = second
    return (min_diff_first, min_diff_second)

