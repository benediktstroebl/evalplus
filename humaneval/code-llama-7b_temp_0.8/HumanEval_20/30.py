from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Find the minimum
    min_number = float('inf')
    for number in numbers:
        if number < min_number:
            min_number = number

    # Find the max number that is at least as close to the min number as all the others
    max_number = float('-inf')
    for number in numbers:
        if abs(number - min_number) > abs(max_number - min_number):
            max_number = number

    return min_number, max_number

