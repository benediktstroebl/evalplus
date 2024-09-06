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
        raise ValueError("list must have length greater than 1")

    smallest_num = float("inf")
    smallest_num_idx = None
    second_closest_num = float("inf")
    second_closest_num_idx = None

    for idx, number in enumerate(numbers):
        if number < smallest_num:
            second_closest_num = smallest_num
            second_closest_num_idx = smallest_num_idx
            smallest_num = number
            smallest_num_idx = idx
        else:
            second_closest_num = number
            second_closest_num_idx = idx

    return smallest_num, second_clos
