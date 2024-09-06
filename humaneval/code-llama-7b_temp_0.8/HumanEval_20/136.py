from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Length of list must be at least two.")

    closest_numbers = (float("inf"), float("inf"))
    for number in numbers:
        for number_to_compare in numbers:
            if abs(number - number_to_compare) < abs(closest_numbers[0] - closest_numbers[1]):
                closest_numbers = (number, number_to_compare)
    return closest_numbers

