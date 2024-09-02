from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    diffs = [(abs(num1 - num2), num1, num2) for num1, num2 in zip(numbers[:-1], numbers[1:])]
    diffs = sorted(diffs)
    if diffs[0][0] < diffs[1][0]:
        return diffs[1][1:], diffs[0][1:]
    else:
        return diffs[0][1:], diffs[1][1
