from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_idx = 0
    min_val = numbers[0]

    for idx, val in enumerate(numbers):
        if val < min_val:
            min_idx = idx
            min_val = val

    max_idx = 0
    max_val = numbers[0]

    for idx, val in enumerate(numbers):
        if idx!= min_idx and val > max_val:
            max_idx = idx
            max_val = val

    return numbers[min_idx], numbers[max_idx]

