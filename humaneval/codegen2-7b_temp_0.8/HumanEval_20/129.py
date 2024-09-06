from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    best_diff = abs(numbers[0] - numbers[1])
    best_numbers = []
    for n in numbers:
        diff = abs(n - numbers[0])
        if diff < best_diff:
            best_diff = diff
            best_numbers = [n]
        elif diff == best_diff:
            best_numbers.append(n)
    return (best_numbers[0], best_numbers[-1])

