from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        return None, None
    left_min, left_max = numbers[0], numbers[0]
    right_min, right_max = numbers[0], numbers[-1]
    for i in range(1, n):
        for j in range(i, n):
            right_min = min(right_min, numbers[j])
            right_max = max(right_max, numbers[j])
            left_max = max(left_max, numbers[i])
            left_min = min(left_min, numbers[i])

    return left_min, right_max

