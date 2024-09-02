from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_numbers = []
    min_abs = float('inf')
    for num in numbers:
        abs_num = abs(num)
        if abs_num < min_abs:
            min_abs = abs_num
            closest_numbers = [num]
        elif abs_num == min_abs:
            closest_numbers.append(num)
    return closest_numbers

