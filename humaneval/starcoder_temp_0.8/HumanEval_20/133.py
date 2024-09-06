from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # This could be done in one line
    # return sorted(numbers)[0::2]

    # Or it can be done in two
    smallest = min(numbers)
    largest = max(numbers)

    if largest - smallest < 0.1:
        return smallest, largest

    return min(numbers, key=lambda x: abs(x - smallest)), max(
        numbers, key=lambda x: abs(x - largest)
    )

