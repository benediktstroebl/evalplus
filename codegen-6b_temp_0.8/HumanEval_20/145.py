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
        raise ValueError("List must contain at least two elements.")

    closest_pair = (_last_element_pair(numbers): [-1, -1])
    for num in numbers:
        new_pair = (num, closest_pair[0]) if abs(num - closest_pair[0]) < abs(num - closest_pair[1]) else (
            closest_pair[1], num)
        closest_pair = new_pair

    return closest_pair

