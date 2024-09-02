from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    difference = abs(numbers[0] - numbers[1])
    smaller = numbers[0]
    larger = numbers[1]
    for x in numbers:
        current = abs(smaller - x)
        if current < difference:
            difference = current
            larger = x
        elif current == difference and x > larger:
            larger = x
    return smaller, larger

