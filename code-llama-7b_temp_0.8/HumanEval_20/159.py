from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # This could be done in one statement, but it is broken up
    # in stages for readability
    minimum_difference = float("inf")
    first_element = None
    second_element = None

    for index, element in enumerate(numbers):
        # Ignore the first element
        if index == 0:
            continue

        # Compute the absolute difference between the element and the previous one
        difference = abs(numbers[index] - numbers[index-1])
        if difference < minimum_difference:
            minimum_difference = difference
            first_element = numbers[index-1]
            second_element = numbers[index]

    return (first_element, second_element)

