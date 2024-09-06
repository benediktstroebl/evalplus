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
        return 0, 0

    small_val, large_val = min(numbers), max(numbers)
    small_index, large_index = numbers.index(small_val), numbers.index(large_val)

    if abs(large_val - small_val) < abs(large_val - numbers[small_index]):
        return large_val, small_val
    return small_val, large
