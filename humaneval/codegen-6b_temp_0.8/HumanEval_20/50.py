from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    first_number = numbers[0]
    second_number = numbers[1]
    smallest_distance = abs(first_number - second_number)
    closest_numbers = (first_number, second_number)
    for i in range(2, len(numbers)):
        number = numbers[i]
        distance = abs(first_number - number)
        if distance < smallest_distance:
            smallest_distance = distance
            closest_numbers = (first_number, number)
        elif distance == smallest_distance:
            closest_numbers = (closest_numbers[0], closest_numbers[1], number)
        first_number = number
    return closest_numbers

