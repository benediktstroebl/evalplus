from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_length = len(numbers)
    if numbers_length < 2:
        raise ValueError("List must be of length greater than 1")
    first_number = numbers[0]
    second_number = numbers[1]
    closest_numbers = [first_number, second_number]
    absolute_difference_first = abs(first_number - second_number)
    for number in numbers[2:]:
        absolute_difference_second = abs(number - first_number)
        if absolute_difference_second < absolute_difference_first:
            absolute_difference_first = absolute_difference_second
            closest_numbers[1] = first_number
            closest_numbers[0] = number
        absolute_difference_second = abs(number - second_number)
        if absolute_difference_second < absolute_difference_first:
            absolute_difference_first = absolute_difference_second
            closest_numbers[1] = second_number
            closest_numbers[0] = number
    return closest_numbers[0], closest_numbers[1]

