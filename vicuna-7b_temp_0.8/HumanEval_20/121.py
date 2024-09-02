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
        raise ValueError("Supplied list of numbers must contain at least two elements.")

    smallest_diff = float('inf')
    smallest_diff_idx = -1
    closest_pair = (float('inf'), float('-inf'))

    for i, number in enumerate(numbers):
        diff = abs(numbers[i+1] - number)
        if diff < smallest_diff:
            smallest_diff = diff
            smallest_diff_idx = i

    return numbers[smallest_diff_idx], numbers[smallest_diff_idx+1]

