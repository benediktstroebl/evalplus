from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        # odd number of elements
        left, right = numbers[:midpoint], numbers[midpoint:]
    else:
        # even number of elements
        left, right = numbers[:midpoint - 1], numbers[midpoint + 1:]
    return get_closest_numbers(left, right)

