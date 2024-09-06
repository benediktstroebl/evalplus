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
        return (numbers[0], numbers[0])
    min_diff = float('inf')
    min_diff_index = 0
    min_diff_value = numbers[0]
    for index in range(1, len(numbers)):
        diff = numbers[index] - numbers[min_diff_index]
        if diff < min_diff:
            min_diff = diff
            min_diff_index = index
            min_diff_value = numbers[min_diff_index]
    return min_diff_value, min_diff_index

