from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        return n, n
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if smallest == numbers[0]:
            smallest = num
            largest = numbers[0]
        elif smallest > num:
            largest = smallest
            smallest = num
    if smallest != numbers[0]:
        largest = largest - (largest - smallest)
    return smallest, largest