from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_diff = None
    smaller_number = None
    larger_number = None
    for (i, m) in enumerate(numbers):
        for n in numbers[i + 1 :]:
            diff = abs(m - n)
            if smallest_diff is None or diff < smallest_diff:
                smallest_diff = diff
                smaller_number = m
                larger_number = n
    return (smaller_number, larger_number)

