from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) == 0:
        raise Exception("There should be at least two numbers in the list!")
    closest_tuple = (sorted_numbers[0], sorted_numbers[1])
    for current_num in sorted_numbers[2:]:
        if abs(current_num - closest_tuple[0]) < abs(current_num - closest_tuple[1]):
            closest_tuple = (current_num, closest_tuple[1])
        else:
            closest_tuple = (closest_tuple[0], current_num)
    return closest_tuple

