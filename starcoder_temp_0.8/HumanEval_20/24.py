from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Find the minimum element of the list
    minimum = numbers[0]

    # Go through the list, finding the element closest to the minimum
    for element in numbers:
        if element < minimum:
            minimum = element

    # Create a list of tuples, each containing a number and its distance from the minimum
    tuples = []
    for element in numbers:
        tuples.append((element, abs(element - minimum)))

    # Sort the list of tuples by their distance from the minimum
    tuples.sort(key=lambda element: element[1])

    return tuples[0][0], tuples[1][0]
