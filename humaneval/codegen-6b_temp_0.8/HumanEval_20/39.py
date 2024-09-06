from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    closest1 = numbers[0]
    closest2 = numbers[0]
    closest1_index = 0
    closest2_index = 0
    for index, number in enumerate(numbers):
        if abs(number - closest1) < abs(number - closest2):
            closest2 = number
            closest2_index = index
        else:
            closest1 = number
            closest1_index = index
    return closest1, closest2

