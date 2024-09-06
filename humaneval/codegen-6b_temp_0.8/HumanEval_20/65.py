from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_difference: float = float("inf") # costly?
    smallest_pair: Tuple[float, float] = None
    for number1 in numbers:
        for number2 in numbers:
            difference = abs(number1 - number2)
            if difference < smallest_difference:
                smallest_difference = difference
                smallest_pair = number1, number2
    return smallest_pair

