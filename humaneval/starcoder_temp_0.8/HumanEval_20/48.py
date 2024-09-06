from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_difference = float('inf')
    left_index = -1
    right_index = -1
    for index, number in enumerate(numbers):
        difference = abs(number - numbers[index + 1])
        if difference < smallest_difference:
            smallest_difference = difference
            left_index = index
            right_index = index + 1
    return numbers[left_index], numbers[right_index]

