from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    # assert len(numbers) >= 2, "List must have a length of at least 2"
    closest = numbers[0], numbers[1]
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) < abs(closest[1] - closest[0]):
            closest = numbers[i - 1], numbers[i]
    return closest

