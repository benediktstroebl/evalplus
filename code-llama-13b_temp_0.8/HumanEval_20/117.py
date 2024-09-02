from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float("inf")
    result_a = None
    result_b = None
    for i in range(len(numbers) - 1):
        a = numbers[i]
        b = numbers[i + 1]
        if abs(a - b) < min_diff:
            min_diff = abs(a - b)
            result_a = min(a, b)
            result_b = max(a, b)
    return result_a, result_b

