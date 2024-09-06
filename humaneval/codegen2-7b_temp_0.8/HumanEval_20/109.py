from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    lowest_diff = sys.float_info.max
    lowest_num = None
    lowest_idx = 0
    for i in range(0, len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < lowest_diff:
            lowest_diff = diff
            lowest_num = numbers[i]
            lowest_idx = i
    return lowest_num, lowest_id
