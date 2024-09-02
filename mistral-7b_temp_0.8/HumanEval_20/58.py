from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # get the smallest two elements and check for the smallest difference between them
    smallest_difference = None
    first_number = None
    second_number = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            if smallest_difference is None or difference < smallest_difference:
                smallest_difference = difference
                first_number = numbers[i]
                second_number = numbers[j]

    return first_number, second_number
