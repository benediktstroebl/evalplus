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
        raise ValueError('List must contain at least two elements')
    min_diff = 1000
    current_min_diff = 0
    current_min_num = 0
    current_max_num = 0
    for number in numbers:
        if number > current_max_num:
            current_max_num = number
        elif number < current_min_num:
            current_min_num = number
        if number < current_min_num + min_diff and number > current_min_num - min_diff:
            current_min_diff = number - current_min_num
            current_max_num = number
        elif number > current_max_num - min_diff and number < current_max_num + min_diff:
            current_min_diff = current_max_num - number
            current_min_num = number
    return current_min_num, current_max_num

