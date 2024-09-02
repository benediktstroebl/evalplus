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
        raise ValueError("Must have at least two numbers.")
    min_val, max_val = numbers[0], numbers[-1]
    min_index = 0
    max_index = len(numbers) - 1
    while min_index <= max_index:
        mid_val = numbers[min_index]
        mid_index = (min_index + max_index) // 2
        distance = abs(mid_val - min_val)
        if distance < abs(mid_val - max_val):
            max_index = mid_index
        else:
            min_index = mid_index
    return min_val, max_val

