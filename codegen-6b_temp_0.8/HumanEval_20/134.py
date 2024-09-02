from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # TODO: Replace this code with a faster algorithm
    difference_1 = abs(numbers[0] - numbers[1])
    difference_2 = abs(numbers[1] - numbers[2])
    difference_3 = abs(numbers[0] - numbers[2])
    differences = [difference_1, difference_2, difference_3]
    closest_numbers = [numbers[0], numbers[1], numbers[2]]
    closest_index = differences.index(min(differences))
    closest_numbers[closest_index] = numbers[closest_index]
    return tuple(closest_numbers)

