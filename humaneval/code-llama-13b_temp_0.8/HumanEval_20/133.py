from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    x = numbers[0]
    y = numbers[-1]
    result = numbers[0]
    delta = y - x
    for i in numbers[1:]:
        x = y
        y = i
        if (y - x) < delta:
            result = x
            result2 = y
            delta = y - x
    return result, result2

