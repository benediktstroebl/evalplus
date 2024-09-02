from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    assert len(numbers) >= 2, "numbers must have at least two elements"

    sorted_numbers = sorted(numbers)

    smallest_diff = sorted_numbers[1] - sorted_numbers[0]
    largest_diff = sorted_numbers[-1] - sorted_numbers[-2]

    if smallest_diff <= largest_diff:
        return sorted_numbers[0], sorted_numbers[1]
    else:
        return sorted_numbers[-2], sorted_numbers[-1]

