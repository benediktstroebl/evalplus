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
        raise ValueError("The input list must contain at least two numbers.")

    smallest_number = numbers[0]
    closest_number_one = smallest_number
    closest_number_two = smallest_number
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
            closest_number_one = smallest_number
            closest_number_two = smallest_number
        else:
            smallest_number = number

    closest_number_one = smallest_number - 1
    closest_number_two = smallest_number + 1

    return closest_number_one, closest_number_two
