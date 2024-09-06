from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_numbers = [float("inf")] * 2
    result = [float("inf")] * 2
    for index, number in enumerate(numbers):
        if number < closest_numbers[1]:
            closest_numbers[0] = closest_numbers[1]
            closest_numbers[1] = number
            result[1] = number
        if number < closest_numbers[0] and number > closest_numbers[1]:
            closest_numbers[0] = number
    result[0] = closest_numbers[0]
    return tuple(result)

