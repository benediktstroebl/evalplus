from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    first_closest, second_closest = numbers[0], numbers[0]
    for num in numbers[1:]:
        if num < first_closest:
            first_closest = num
        elif num > first_closest:
            first_closest = num
        elif num < second_closest:
            second_closest = num
        elif num > second_closest:
            second_closest = num
    return first_closest, second_closest

