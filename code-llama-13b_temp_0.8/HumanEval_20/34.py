from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # We will need to keep track of the two closest numbers.
    # We will also need to keep track of their absolute difference.
    # When we see a new number we will compare it with the first closest number, and if the absolute difference is
    # smaller than the current smallest absolute difference, we will update the two closest numbers.
    # When we see a new number we will compare it with the second closest number, and if the absolute difference is
    # smaller than the current smallest absolute difference, we will update the two closest numbers.
    # Finally we will return the two closest numbers.

    closest_1 = numbers[0]
    closest_2 = numbers[1]

    closest_difference = abs(closest_1 - closest_2)

    for number in numbers:
        if abs(number - closest_1) < closest_difference:
            closest_difference = abs(closest_1 - number)
            closest_2 = closest_1
            closest_1 = number
        elif abs(number - closest_2) < closest_difference:
            closest_difference = abs(closest_2 - number)
            closest_1 = closest_2
            closest_2 = number

    return closest_1, closest_2

