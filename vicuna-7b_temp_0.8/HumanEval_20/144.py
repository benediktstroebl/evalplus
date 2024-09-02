from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")

    smallest = numbers[0]
    second_smallest = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
        if numbers[i] < second_smallest and second_smallest != smallest:
            second_smallest = numbers[i]

    return smallest, second_smallest