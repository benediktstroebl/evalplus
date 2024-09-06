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
        raise ValueError('Less than two elements.')

    closest_elements: Tuple[float, float] = (numbers[0], numbers[1])

    for i in range(1, list_length):
        if numbers[i] < closest_elements[0]:
            closest_elements = (numbers[i], closest_elements[0])

        if numbers[i] < closest_elements[1]:
            closest_elements = (closest_elements[1], numbers[i])

    return closest_elements
