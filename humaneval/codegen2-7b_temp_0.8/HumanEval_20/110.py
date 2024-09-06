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
        raise ValueError("not enough values in array")

    min_idx = 0
    min_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min_val:
            min_idx = i
            min_val = numbers[i]
    max_idx = 0
    max_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_idx = i
            max_val = numbers[i]
    return numbers[min_idx], numbers[max_id
