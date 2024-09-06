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
        return 0, 0
    min_diff = 0.0
    min_diff_index = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            diff = numbers[i] - numbers[j]
            min_diff = min(min_diff, diff)
            if min_diff < min_diff_index:
                min_diff_index = min_diff
    return numbers[min_diff_index], numbers[n - min_diff_index]

