from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    smallest = numbers[0]
    largest = numbers[-1]
    for i in range(1, len(numbers)):
        if numbers[i]!= smallest:
            smallest = numbers[i]
            break
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i]!= largest:
            largest = numbers[i]
            break
    return smallest, largest

