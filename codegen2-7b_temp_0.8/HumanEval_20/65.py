from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest = float("inf")
    closest_to_smallest = None
    closest_to_largest = None

    for x in numbers:
        if x < smallest:
            closest_to_smallest = x
            closest_to_largest = smallest
            smallest = x
        elif x == smallest:
            closest_to_smallest = x
            closest_to_largest = x
        elif x > smallest:
            closest_to_largest = x

    return closest_to_smallest, closest_to_
