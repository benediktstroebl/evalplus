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
        raise ValueError('find_closest_elements needs at least two numbers')

    elements = sorted(numbers)
    difference = elements[1] - elements[0]
    for i in range(len(numbers) - 1):
        d = elements[i + 1] - elements[i]
        if d < difference:
            difference = d
            closest = elements[i + 1]
            second_closest = elements[i]

    return second_closest, closest

