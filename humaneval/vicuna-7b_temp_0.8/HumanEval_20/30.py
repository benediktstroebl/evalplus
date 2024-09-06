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
    min_num = float('-inf')
    min_diff_index = 0
    min_diff_elem = numbers[0]
    min_diff_elem_idx = 0

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        num = numbers[i]

        if abs(diff) < min_diff:
            min_diff = abs(diff)
            min_diff_elem = numbers[i]
            min_diff_elem_idx = i

        elif abs(diff) < min_diff and abs(diff) < min_num:
            min_num = num

    return min_diff_elem, min_num

