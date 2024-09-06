from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    a = numbers[0]
    b = numbers[1]
    closest = numbers[0]

    for number in numbers[1:]:
        if abs(a - number) < abs(b - number):
            b = number
        elif abs(a - number) >= abs(b - number):
            a = number
    return (a, b)

