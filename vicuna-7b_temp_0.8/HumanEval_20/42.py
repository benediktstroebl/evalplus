from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    largest_distance = float('inf')
    smallest_distance = float('-inf')
    largest = None
    smallest = None
    for num in numbers:
        distance = abs(num - (largest or 0.0))
        if largest is None or distance < largest_distance:
            largest = num
            largest_distance = distance
        if smallest is None or distance < smallest_distance:
            smallest = num
            smallest_distance = distance
    return smallest, largest

