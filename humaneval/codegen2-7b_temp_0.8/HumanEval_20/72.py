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
        raise ValueError("The list must contain at least two numbers")

    closest_indices = [0, 0]
    for idx, num in enumerate(numbers):
        if num == closest_indices[0] or num == closest_indices[1]:
            continue
        if abs(num - closest_indices[0]) > abs(num - closest_indices[1]):
            closest_indices[1] = closest_indices[0]
            closest_indices[0] = num
        else:
            closest_indices[1] = num

    return closest_indices[0], closest_indices[1
