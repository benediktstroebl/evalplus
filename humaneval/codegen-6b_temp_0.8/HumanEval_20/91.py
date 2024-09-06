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
    # default to the first two elements if the list is too short
    # but if faster than the first two...
    if len(sorted_numbers) < 2:
        return sorted_numbers[0], sorted_numbers[1]
    else:
        diff1 = abs(sorted_numbers[0] - sorted_numbers[1])
        diff2 = abs(sorted_numbers[0] - sorted_numbers[-1])
        if diff1 < diff2:
            return sorted_numbers[0], sorted_numbers[1]
        elif diff1 > diff2:
            return sorted_numbers[-1], sorted_numbers[-2]
        elif diff1 == diff2:
            return sorted_numbers[0], sorted_numbers[-1]

