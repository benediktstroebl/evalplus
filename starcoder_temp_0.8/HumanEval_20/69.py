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
        return None
    sorted_numbers = sorted(numbers)
    smallest_difference = sorted_numbers[1] - sorted_numbers[0]
    for i in range(2, len(sorted_numbers)):
        if sorted_numbers[i] - sorted_numbers[i - 1] < smallest_difference:
            smallest_difference = sorted_numbers[i] - sorted_numbers[i - 1]
            smallest_index = i - 1
            biggest_index = i
    return sorted_numbers[smallest_index], sorted_numbers[biggest_index]

