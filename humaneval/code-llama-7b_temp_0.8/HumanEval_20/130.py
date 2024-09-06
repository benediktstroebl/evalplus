from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_difference = None
    min_numbers = None

    for number_1 in numbers:
        for number_2 in numbers:
            if number_1 == number_2:
                continue
            difference = abs(number_1 - number_2)
            if min_difference is None or difference < min_difference:
                min_difference = difference
                min_numbers = (number_1, number_2)
    return min_numbers

