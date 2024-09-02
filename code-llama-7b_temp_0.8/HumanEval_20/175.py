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
    min_a = numbers[0]
    min_b = numbers[1]
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if i != j:
                diff = abs(a - b)
                if diff < min_diff:
                    min_diff = diff
                    min_a = a
                    min_b = b

    return min_a, min_b

