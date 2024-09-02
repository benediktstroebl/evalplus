from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # NOTE: numbers.sort() already does what we need here
    highest, lowest = find_highest_and_lowest(numbers)
    delta_highest = numbers[numbers.index(highest)] - highest
    delta_lowest = lowest - numbers[numbers.index(lowest)]
    if delta_highest < delta_lowest:
        return lowest, highest

    return highest, lowest

