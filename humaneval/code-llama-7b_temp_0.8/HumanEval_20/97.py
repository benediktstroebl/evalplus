from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # find the smallest distance between any two elements
    min_distance = min(abs(a - b) for a in numbers for b in numbers)
    # find the indices of the two numbers that are at the minimum distance
    min_indices = [
        numbers.index(a)
        for a in numbers
        if abs(a - numbers[numbers.index(a) + 1]) == min_distance
    ]
    # return the two numbers at those indices
    return (numbers[min_indices[0]], numbers[min_indices[1]])

