from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    best_num1, best_num2 = float("inf"), float("inf")
    min_diff = float("inf")

    for num1, num2 in numbers:
        diff = abs(num1 - num2)
        if diff < min_diff:
            min_diff = diff
            closest_diff = min_diff
            closest_num1, closest_num2 = num1, num2

    return closest_num1, closest_num2

