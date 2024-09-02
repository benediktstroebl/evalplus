from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_list = sorted(numbers)
    min_diff = abs(sorted_list[1] - sorted_list[0])
    first_number = sorted_list[0]
    second_number = sorted_list[1]
    for i in range(len(sorted_list)):
        diff = abs(sorted_list[i + 1] - sorted_list[i])
        if diff < min_diff:
            min_diff = diff
            first_number = sorted_list[i]
            second_number = sorted_list[i + 1]
    return first_number, second_number
