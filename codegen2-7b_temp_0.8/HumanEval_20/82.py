from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    dists = [(abs(x - y), x, y) for x, y in zip(numbers, numbers[1:])]
    smaller_index, smaller_number = min(dists, key=lambda tup: tup[0])
    bigger_index, bigger_number = max(dists, key=lambda tup: tup[0])
    return smaller_number, bigger_number
