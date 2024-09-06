from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = 100000000
    closest_numbers = [0, 0]
    for num in numbers:
        if num not in numbers:
            continue
        else:
            for num2 in numbers:
                if num == num2:
                    continue
                else:
                    diff = abs(num - num2)
                    if diff < min_diff:
                        min_diff = diff
                        closest_numbers = [num, num2]
    return closest_numbers

