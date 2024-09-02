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

    min_val = numbers[0]
    min_idx = 0
    for idx in range(1, n):
        if numbers[idx] < min_val:
            min_val = numbers[idx]
            min_idx = idx

    max_val = numbers[n - 1]
    max_idx = n - 1
    for idx in range(0, n - 1):
        if numbers[idx] > max_val:
            max_val = numbers[idx]

    closest_pair = (min_val, max_val)
    return closest_pair[0], closest_pair[1]

