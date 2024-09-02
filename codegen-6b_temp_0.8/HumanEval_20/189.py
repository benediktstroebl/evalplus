from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n_numbers = len(numbers)
    if n_numbers < 2:
        raise ValueError("At least two elements are required")

    # sort the list, select the two closest numbers, and return them in order
    sorted_numbers = sorted(numbers)
    if n_numbers == 2:
        return sorted_numbers

    to_closest = sorted_numbers[1] - sorted_numbers[0]

    # do modulo modulo operator
    for i in range(1, n_numbers - 1):
        current_diff = sorted_numbers[i+1] - sorted_numbers[i]
        if abs(current_diff) < abs(to_closest):
            to_closest = current_diff

    return sorted_numbers[0], sorted_numbers[-1]

