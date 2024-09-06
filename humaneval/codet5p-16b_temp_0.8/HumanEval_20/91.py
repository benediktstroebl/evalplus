from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    first_closest = None
    second_closest = None
    for index, first in enumerate(numbers):
        for second in numbers[index + 1:]:
            if first > second:
                first, second = second, first
            if first_closest is None or second_closest is None:
                first_closest = first
                second_closest = second
            else:
                if first - first_closest < second - second_closest:
                    second_closest = second
                elif first - first_closest > second - second_closest:
                    first_closest = first
    return first_closest, second_closest
    
