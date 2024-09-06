from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest = math.inf
    smallest_index = 0
    largest = -math.inf
    largest_index = 0
    for i, number in enumerate(numbers):
        if number < smallest:
            smallest = number
            smallest_index = i
        if number > largest:
            largest = number
            largest_index = i
    return smallest_index, largest_index

