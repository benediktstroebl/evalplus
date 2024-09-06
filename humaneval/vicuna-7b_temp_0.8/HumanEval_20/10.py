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
        raise ValueError("Cannot find closest elements as the list has only one element.")

    min_distance = float('inf')
    min_a, min_b = float('-inf'), float('inf')
    for a in numbers:
        for b in numbers:
            distance = abs(a - b)
            if distance < min_distance:
                min_distance = distance
                min_a = a
                min_b = b

    return min_a, min_b

