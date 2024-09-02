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
        raise ValueError("numbers must have at least two elements")
    first, *others, last = numbers
    first_is_closest = True
    for other in others:
        if other < first:
            second = first
            first = other
            first_is_closest = False
        elif other < last:
            second = last
            last = other
    return first, second if first_is_closest else last, second
