from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float('inf')
    min_diff_val = None
    min_diff_val_index = None
    smallest_num = numbers[0]
    smallest_diff = numbers[0]
    for i in range(1, len(numbers)):
        smallest_diff_val = numbers[i]
        smallest_diff = min(smallest_diff, abs(smallest_num - numbers[i]))
        if abs(smallest_diff) < min_diff:
            min_diff, min_diff_val, min_diff_val_index = smallest_diff, i, smallest_num
    return min_diff_val, min_diff_val_index

