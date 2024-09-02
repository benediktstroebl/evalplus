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
    result = None
    for num1 in numbers:
        for num2 in numbers:
            if num1 == num2:
                continue
            if diff is None or abs(num1 - num2) < diff:
                diff = abs(num1 - num2)
                result = (num1, num2)
    return result

