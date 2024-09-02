from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return None

    min_diff = float('inf')
    min_val = float('inf')
    max_val = float('-inf')

    for x in numbers:
        for y in numbers:
            diff = abs(x - y)
            val = x

            if diff < min_diff:
                min_diff = diff
                min_val = val
            elif diff == min_diff:
                if val < max_val:
                    max_val = val

    return min_val, max_val

