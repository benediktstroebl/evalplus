from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    left_i, right_i, left_diff, right_diff = None, None, None, None
    for i, n in enumerate(numbers):
        diff = abs(n - numbers[(i + 1) % len(numbers)])
        if not left_i or diff < left_diff:
            left_i, left_diff = i, diff
        if not right_i or diff < right_diff:
            right_i, right_diff = i, diff
    return numbers[left_i], numbers[right_i]
