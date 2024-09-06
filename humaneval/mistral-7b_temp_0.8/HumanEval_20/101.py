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
        raise ValueError("numbers must be of length >= 2")

    sorted_numbers = sorted(numbers)
    smallest_diff = abs(sorted_numbers[1] - sorted_numbers[0])
    closest_elems = (sorted_numbers[0], sorted_numbers[1])
    for i in range(len(sorted_numbers) - 2):
        diff = abs(sorted_numbers[i+2] - sorted_numbers[i+1])
        if diff < smallest_diff:
            closest_elems = (sorted_numbers[i+1], sorted_numbers[i+2])
            smallest_diff = diff
    return closest_elems

