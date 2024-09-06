from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return None, None
    if not numbers:
        return None, None

    smallest_difference = max(numbers)
    smallest_index = 0
    smallest_number = numbers[0]

    for index in range(1, len(numbers)):
        second_smallest_difference = max(numbers[index - 1], numbers[index])
        second_smallest_index = index
        second_smallest_number = numbers[index]
        if smallest_difference - second_smallest_difference > 0.1:
            smallest_difference = second_smallest_difference
            smallest_index = second_smallest_index
            smallest_number = second_smallest_number

    return smallest_number, smallest_index