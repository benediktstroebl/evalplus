from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    first_number: float
    second_number: float
    minimum_distance: float
    minimum_distance_index: int
    first_number = numbers[0]
    second_number = numbers[1]
    minimum_distance = abs(first_number - second_number)
    minimum_distance_index = 0
    for index in range(0, len(numbers) - 1):
        for index2 in range(index + 1, len(numbers)):
            if abs(numbers[index] - numbers[index2]) < minimum_distance:
                minimum_distance = abs(numbers[index] - numbers[index2])
                minimum_distance_index = index
    return (numbers[minimum_distance_index], numbers[minimum_distance_index + 1])
    pass
