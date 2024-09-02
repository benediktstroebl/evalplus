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
        return n, n
    closest = numbers
    smallest, closest = closest, closest[0]
    for i in range(1, n-1):
        if smallest > closest:
            smallest = closest
            closest = closest[0]
        elif smallest < closest:
            smallest = closest
            closest = closest[0]
    return smallest, closest