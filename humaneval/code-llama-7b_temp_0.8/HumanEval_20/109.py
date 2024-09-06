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
        raise ValueError('The supplied list must have a length greater than 2.')

    sorted_list = sorted(numbers)

    # Initializing the first two closest numbers
    first_closest = sorted_list[0]
    second_closest = sorted_list[1]

    # Iterating over the sorted list and finding the closest numbers
    for number in sorted_list[2:]:
        if abs(number - sorted_list[0]) < abs(number - sorted_list[1]):
            first_closest = number
        else:
            second_closest = number

    return first_closest, second_closest

