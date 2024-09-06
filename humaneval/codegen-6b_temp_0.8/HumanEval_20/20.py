from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    length = len(numbers)
    sorted_numbers = sorted(numbers)
    closest_to_2_and_1 = sorted_numbers[0]
    closest_to_2_and_3 = sorted_numbers[length - 1]
    return (closest_to_2_and_1, closest_to_2_and_3)

