from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_difference = float("inf")
    first_number = None
    second_number = None

    for i, number in enumerate(numbers):
        for j, number2 in enumerate(numbers):
            if j > i:
                difference = abs(number - number2)
                if difference < min_difference:
                    min_difference = difference
                    first_number = number
                    second_number = number2

    return (first_number, second_number)
