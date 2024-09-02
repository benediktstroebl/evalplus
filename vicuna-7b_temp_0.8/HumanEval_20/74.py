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
    min_diff_other = float('inf')
    min_other = float('inf')
    min_other_number = float('inf')
    min_diff_other_number = float('inf')
    for n in numbers:
        diff = abs(n - min(numbers))
        if diff < min_diff:
            min_diff = diff
            min_diff_other = min_diff_other
            min_other = n
            min_other_number = min_other
            min_diff_other_number = diff
    return min_other, min_other_number