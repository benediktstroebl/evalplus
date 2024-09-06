from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # finding the absolute closest elements is the same as finding the two closest numbers
    # to the average of the list. this is because if we have two points, one close to the average
    # and one far from it, their difference will always be less than the difference of two points
    # with the average somewhere in between.
    if len(numbers) < 2:
        raise ValueError("List must have at least 2 numbers")
    avg = sum(numbers) / len(numbers)
    return min(numbers), max(x for x in numbers if abs(x - avg) == abs(min(numbers) - avg))

