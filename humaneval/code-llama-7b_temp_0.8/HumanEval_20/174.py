from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Pythonic solution:
    # return sorted(numbers, key=numbers.index)[:2]

    # Original solution:
    idx_smallest_diff = 0
    idx_largest_diff = 1
    current_smallest_diff = numbers[idx_smallest_diff] - numbers[idx_largest_diff]
    for i in range(2, len(numbers)):
        if numbers[idx_smallest_diff] - numbers[i] < current_smallest_diff:
            idx_largest_diff = idx_smallest_diff
            idx_smallest_diff = i
            current_smallest_diff = numbers[idx_smallest_diff] - numbers[idx_largest_diff]
        elif numbers[i] - numbers[idx_largest_diff] < current_smallest_diff:
            idx_largest_diff = i
    return numbers[idx_smallest_diff], numbers[idx_largest_diff]

