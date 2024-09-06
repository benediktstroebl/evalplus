from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Find the closest numbers
    min_diff = None
    smallest_num = None
    smallest_diff = None
    largest_num = None
    largest_diff = None
    for n in numbers:
        diff = abs(n - n // 1)
        if min_diff is None or diff < min_diff:
            min_diff = diff
            smallest_num = n
            smallest_diff = 0
        if diff == min_diff:
            if n < smallest_num:
                smallest_num = n
                smallest_diff = 0
            elif n > smallest_num:
                smallest_num = n
                smallest_diff = 0
        if largest_diff is None or diff > largest_diff:
            largest_num = n
            largest_diff = 0
        if diff == largest_diff:
            if n > largest_num:
                largest_num = n
                largest_diff = 0
            elif n < largest_num:
                largest_num = n
                largest_diff = 0

    return smallest_num, largest_num

