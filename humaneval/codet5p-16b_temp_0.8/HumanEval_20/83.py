from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_diff: float = numbers[1] - numbers[0]
    min1: float = numbers[0]
    min2: float = numbers[1]
    for i in range(2, len(numbers)):
        diff: float = numbers[i] - numbers[i - 1]
        if diff < min_diff:
            min2 = min1
            min1 = numbers[i - 1]
            min_diff = diff
        elif diff < min_diff:
            min2 = numbers[i - 1]
            min_diff = diff
    return min1, min2
