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
    min_val = float('-inf')
    max_val = float('inf')
    for num in numbers:
        diff = abs(num - min_val)
        if diff < min_diff:
            min_diff = diff
            min_val = num
        elif diff > max_diff:
            max_diff = diff
            max_val = num
    return min_val, max_val

