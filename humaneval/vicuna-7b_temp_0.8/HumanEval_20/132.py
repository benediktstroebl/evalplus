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
    min_diff_index = -1
    min_diff_num = 0
    min_diff_num_idx = 0

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i
            min_diff_num = numbers[i]
            min_diff_num_idx = i

    return min_diff_num, min_diff_num_idx

