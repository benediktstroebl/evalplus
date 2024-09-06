from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_diff = float('inf')
    largest_diff = float('-inf')
    smallest_num = float('inf')
    largest_num = float('-inf')
    smallest_num_idx = 0
    largest_num_idx = 0
    for idx in range(1, len(numbers)):
        diff = numbers[idx] - numbers[idx - 1]
        smallest_diff = min(smallest_diff, diff)
        largest_diff = max(largest_diff, diff)
        smallest_num = min(smallest_num, numbers[idx])
        largest_num = max(largest_num, numbers[idx])
        smallest_num_idx = idx
        largest_num_idx = idx
    return smallest_num, largest_num

