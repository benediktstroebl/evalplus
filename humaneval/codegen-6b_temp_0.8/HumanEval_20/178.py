from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)  # implicitly sorts in place
    smallest = sorted_numbers[0]
    largest = sorted_numbers[-1]
    try:
        second_smallest = sorted_numbers[sorted_numbers.index(smallest) - 1]
    except ValueError:
        second_smallest = None
    try:
        second_largest = sorted_numbers[sorted_numbers.index(largest) + 1]
    except ValueError:
        second_largest = None

    if second_smallest == smallest and second_largest == largest:
        raise ValueError('Duplicate numbers provided as input')

    return smallest, second_largest or largest  # second_largest can be None

