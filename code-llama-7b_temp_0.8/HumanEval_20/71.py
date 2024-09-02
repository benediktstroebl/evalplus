from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Initialize minimum distance
    min_distance = None

    # Initialize index of element with minimum distance
    min_index = None
    min_index_two = None

    # Iterate over the list, and update the minimum distance and its index
    for index in range(1, len(numbers)):
        # The distance between the current number and previous number
        distance = abs(numbers[index] - numbers[index - 1])

        # If we don't have a minimum distance yet, update it
        if min_distance is None:
            min_distance = distance
            min_index = index - 1
            min_index_two = index

        # If we have a minimum distance, compare it with the current distance
        elif distance < min_distance:
            min_distance = distance
            min_index = index - 1
            min_index_two = index

    return numbers[min_index], numbers[min_index_two]

