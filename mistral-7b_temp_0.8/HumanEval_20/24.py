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
        raise Exception("Not enough elements")
    min_diff = None
    min_diff_index = None
    min_value = None
    min_value_index = None
    for i, n in enumerate(numbers):
        if min_diff is None or abs(min_diff) > abs(n - min_value):
            min_diff = n - min_value
            min_diff_index = i
            min_value = n
            min_value_index = i

    return min_value, numbers[min_diff_index]
