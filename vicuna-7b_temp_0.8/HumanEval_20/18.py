from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        return None, None

    smallest, smallest_dist = numbers[0], 0.0
    largest, largest_dist = numbers[-1], 0.0
    for num in numbers[1:]:
        dist = abs(num - smallest)
        if dist < smallest_dist:
            smallest, smallest_dist = num, dist
        elif dist < largest_dist:
            largest, largest_dist = num, dist

    return smallest, largest

