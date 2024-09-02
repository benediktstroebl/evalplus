from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_dist, min_val = float('inf'), None
    min_vals = []
    for val in numbers:
        if val is None or val == min_val:
            min_dist = 0
        else:
            dist = abs(val - min_val)
            min_dist = min(min_dist, dist)
            min_vals.append(val)
    return min_vals[0], min_vals[1]

