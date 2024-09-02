from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest = None, None
    for i, m in enumerate(numbers[1:]):
        if closest[0] is None or abs(closest[0] - m) < abs(closest[1] - m):
            if closest[1] is not None and abs(closest[0] - m) == abs(closest[1] - m):
                closest = i, closest[1]
            else:
                closest = i, m
    return closest

