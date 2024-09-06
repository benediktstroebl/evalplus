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
        raise ValueError("Less than two items in supplied list.")
    else:
        min_num1 = min(numbers)
        min_num2 = max(numbers)
        min_num_pair = min(((min_num1, min_num2), abs(min_num1 - min_num2)))
        return min_num_pair[0], min_num_pair[1]

