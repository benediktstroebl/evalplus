from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_diff = sys.float_info.max
    smallest_number = None
    smallest_index = None
    for index, number in enumerate(numbers):
        diff = abs(number - smallest_diff)
        if diff < smallest_diff:
            smallest_diff = diff
            smallest_number = number
            smallest_index = index
    return smallest_number, numbers[smallest_index
