from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    diff = None
    value_1 = None
    value_2 = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            if diff is None or difference < diff:
                diff = difference
                value_1 = numbers[i]
                value_2 = numbers[j]
    return value_1, value_2

