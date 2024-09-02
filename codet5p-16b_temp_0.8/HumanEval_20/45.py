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
    first_number, second_number = numbers[0], numbers[1]
    closest_first_second_distance = abs(first_number - second_number)
    for first_index in range(len(numbers) - 1):
        for second_index in range(first_index + 1, len(numbers)):
            first_number = numbers[first_index]
            second_number = numbers[second_index]
            current_distance = abs(first_number - second_number)
            if current_distance < closest_first_second_distance:
                closest_first_second_distance = current_distance
                closest_first_second_numbers = (first_number, second_number)
    return closest_first_second_numbers

