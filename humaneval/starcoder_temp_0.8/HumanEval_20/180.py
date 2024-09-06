from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    numbers_sorted = sorted(numbers)
    closest = (numbers_sorted[0], numbers_sorted[1])

    for number in numbers_sorted[2:]:
        distance_to_closest = abs(closest[0] - number)
        distance_to_second_closest = abs(closest[1] - number)

        if distance_to_closest < distance_to_second_closest:
            closest = (closest[0], number)
        else:
            closest = (closest[1], number)

    return closest

