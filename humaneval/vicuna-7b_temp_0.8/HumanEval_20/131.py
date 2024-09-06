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
    min_val = float('-inf')
    max_val = float('inf')
    min_index = -1
    max_index = -1
    for i, num in enumerate(numbers):
        for j in range(i):
            diff = abs(num - numbers[j])
            if diff < min_diff:
                min_diff = diff
                min_val = min(min_val, num)
                min_index = i
                max_index = j
    if min_index < 0:
        return numbers[0], numbers[-1]
    else:
        return numbers[min_index], numbers[max_index]

