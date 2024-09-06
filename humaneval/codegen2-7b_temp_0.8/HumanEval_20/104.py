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
        raise ValueError("Need at least 2 numbers to find the closest")

    index = 0
    closest = None
    for i in range(len(numbers)):
        if closest is None or abs(numbers[i] - closest) > abs(numbers[i] - numbers[index]):
            closest = numbers[i]
            index = i
    return (closest, numbers[index
