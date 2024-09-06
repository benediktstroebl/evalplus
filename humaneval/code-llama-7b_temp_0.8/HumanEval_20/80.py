from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Smallest number
    smallest_number = float("inf")
    for number in numbers:
        if number < smallest_number:
            smallest_number = number

    # Largest number
    largest_number = float("-inf")
    for number in numbers:
        if number > largest_number:
            largest_number = number

    # Find the numbers closest to each other
    return (
        smallest_number,
        largest_number,
    )

