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
    closest_number_1 = numbers[0]
    closest_number_2 = numbers[0]
    closest_distance = numbers[1] - numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] < closest_distance:
            closest_distance = numbers[i] - numbers[i - 1]
            closest_number_1 = numbers[i - 1]
            closest_number_2 = numbers[i]
    return closest_number_1, closest_number_2

