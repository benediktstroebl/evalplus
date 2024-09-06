from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_left = closest_right = numbers[0]
    for i in range(1, len(numbers)):
        diff_left = abs(numbers[i] - closest_left)
        diff_right = abs(numbers[i] - closest_right)
        if diff_left < diff_right:
            closest_left = numbers[i]
        elif diff_left > diff_right:
            closest_right = numbers[i]
        else:
            pass
    return closest_left, closest_right
