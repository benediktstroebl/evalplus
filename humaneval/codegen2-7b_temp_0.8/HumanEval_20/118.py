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
        return -1, -1

    closest_elements = []
    for n1, n2 in zip(numbers[:-1], numbers[1:]):
        diff = n1 - n2
        if diff < 0.0:
            diff *= -1
        if closest_elements and diff < 0.0:
            continue

        closest_elements.append(diff)

    return min(closest_elements), max(closest_elements
