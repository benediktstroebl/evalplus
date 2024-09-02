from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nearest_pair = (None, None)  # type: Tuple[float, float]
    for x in numbers:
        for y in numbers:
            if x != y and (nearest_pair[0] is None or abs(x - y) < abs(nearest_pair[0] - nearest_pair[1]):
                nearest_pair = (x, y)
    return nearest_pair

