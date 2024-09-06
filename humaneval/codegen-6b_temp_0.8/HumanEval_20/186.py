from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_element = min(numbers)
    max_element = max(numbers)
    smallest_difference = None
    for element in numbers:
        difference = abs(min_element - element)
        if smallest_difference is None or difference < smallest_difference:
            smallest_difference = difference

    if smallest_difference is None:
        return None, None

    smallest_element = min_element
    largest_element = max_element
    for element in numbers:
        if element > smallest_element:
            smallest_element = element
        if element < largest_element:
            largest_element = element

    return smallest_element, largest_element

