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
        return None, None

    min_distance = float('inf')
    min_closest_num, min_closest_dist = None, None

    for closest_num, closest_dist in sorted(((n, abs(n - x)) for n, x in zip(numbers, numbers[1:]))):
        if abs(closest_dist) < min_distance:
            min_distance = closest_dist
            min_closest_num, min_closest_dist = closest_num, closest_dist

    return min_closest_num, min_closest_dist

