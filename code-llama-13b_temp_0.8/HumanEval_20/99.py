from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    minimum_distance = abs(numbers[0] - numbers[1])
    first_element = numbers[0]
    second_element = numbers[1]
    for index, number in enumerate(numbers):
        if index + 1 >= len(numbers):
            break
        distance = abs(numbers[index] - numbers[index + 1])
        if distance < minimum_distance:
            minimum_distance = distance
            first_element = numbers[index]
            second_element = numbers[index + 1]
    return first_element, second_element

