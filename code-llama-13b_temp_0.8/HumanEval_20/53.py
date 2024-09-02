from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    list_size = len(numbers)

    if list_size == 0 or list_size == 1:
        raise ValueError("The list must have at least two numbers.")

    closest_numbers = numbers[0], numbers[1]
    closest_numbers_distance = abs(closest_numbers[1] - closest_numbers[0])
    for i in range(list_size - 1):
        for j in range(i + 1, list_size):
            distance_between = abs(numbers[i] - numbers[j])
            if distance_between < closest_numbers_distance:
                closest_numbers_distance = distance_between
                closest_numbers = numbers[i], numbers[j]
    return closest_numbers

