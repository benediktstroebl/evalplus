from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    number_min = min(numbers)
    number_max = max(numbers)

    for number in numbers:
        if number_min < number and number < number_max:
            number_max = number

    for number in numbers:
        if number < number_min and number_min < number_max:
            number_min = number

    return number_min, number_max

