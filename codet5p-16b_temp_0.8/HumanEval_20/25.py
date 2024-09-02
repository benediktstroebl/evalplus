from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    list_length = len(numbers)
    if list_length < 2:
        raise ValueError("List of numbers must contain at least two elements")

    closest_numbers = [numbers[0], numbers[1]]
    closest_distance = abs(numbers[0] - numbers[1])
    for i in range(list_length - 1):
        for j in range(i + 1, list_length):
            if abs(numbers[i] - numbers[j]) < closest_distance:
                closest_distance = abs(numbers[i] - numbers[j])
                closest_numbers = [numbers[i], numbers[j]]

    return tuple(closest_numbers)
