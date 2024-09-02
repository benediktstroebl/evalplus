from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = 10000
    closest_numbers = []
    for number in numbers:
        for other_number in numbers:
            if number == other_number:
                continue
            diff = abs(number - other_number)
            if diff < min_diff:
                min_diff = diff
                closest_numbers = [number, other_number]
    return tuple(sorted(closest_numbers))

