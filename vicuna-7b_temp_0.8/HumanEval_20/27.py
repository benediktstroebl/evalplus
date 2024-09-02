from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("The list of numbers must have at least two elements.")

    min_diff = float('inf')
    min_index1, min_index2 = 0, 0

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[min_index1]
        if diff < min_diff:
            min_diff = diff
            min_index2 = i

    return min_index1, min_index2

