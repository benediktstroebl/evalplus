from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2 or len(numbers) == 2:
        return numbers[0], numbers[1]

    close_to_smallest_number = None
    smallest_number_index = 0
    for i, number in enumerate(numbers):
        if close_to_smallest_number is None or number < close_to_smallest_number:
            smallest_number_index = i
            close_to_smallest_number = number
    close_to_largest_number = None
    close_to_largest_number_index = None
    for i, number in enumerate(numbers):
        if i != smallest_number_index:
            if close_to_largest_number is None or number > close_to_largest_number:
                close_to_largest_number = number
                close_to_largest_number_index = i
    return numbers[smallest_number_index], numbers[close_to_largest_number_index]

