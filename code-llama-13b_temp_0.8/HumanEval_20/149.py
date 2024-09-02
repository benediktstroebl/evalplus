from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_val = max_val = numbers[0]
    prev_min_index = prev_max_index = 0
    for i in range(1, len(numbers)):
        if abs(numbers[i] - min_val) < abs(max_val - min_val):
            max_val = min_val
            min_val = numbers[i]
            prev_max_index = prev_min_index
            prev_min_index = i
        elif abs(numbers[i] - max_val) < abs(max_val - min_val):
            max_val = numbers[i]
            prev_max_index = i
    if prev_min_index == prev_max_index:
        return min_val, max_val
    elif prev_min_index < prev_max_index:
        return numbers[prev_min_index], numbers[prev_max_index]
    else:
        return numbers[prev_max_index], numbers[prev_min_index]

