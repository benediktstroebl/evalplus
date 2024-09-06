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
        raise Exception("Input list must contain at least two elements")
    closest_to_first = None
    closest_to_second = None
    for i, number in enumerate(numbers):
        if closest_to_first is None or number < closest_to_first:
            closest_to_first = number
            closest_to_second = numbers[i + 1]
        elif closest_to_second is None or number < closest_to_second:
            closest_to_second = number
    return closest_to_first, closest_to_
