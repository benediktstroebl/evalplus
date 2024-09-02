from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    closest_pair = sorted_numbers[:2]
    for i in range(len(sorted_numbers) - 2):
        if sorted_numbers[i + 2] - sorted_numbers[i] > closest_pair[1] - closest_pair[0]:
            closest_pair = sorted_numbers[i:i + 2]
    return tuple(closest_pair)

