from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    difference = abs(numbers[0] - numbers[1])
    for index, number in enumerate(numbers):
        if index < len(numbers) - 1:
            current_difference = abs(numbers[index + 1] - number)
            if current_difference < difference:
                difference = current_difference
    return numbers[0], numbers[difference_index + 1
