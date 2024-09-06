from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # verify that the input list contains at least two numbers
    if len(numbers) < 2:
        raise ValueError("List 'numbers' should contain at least two elements")

    # convert the input list to a list of (num, index) pairs
    numbers_with_indexes = [(numbers[i], i) for i in range(len(numbers))]

    # sort the list numerically so we can find the closest numbers in linear time
    numbers_with_indexes.sort(key=lambda pair: pair[0])

    # now find the closest two numbers
    smallest = numbers_with_indexes[0][0]
    largest = numbers_with_indexes[-1][0]
    closest = sorted([smallest, largest])[1]

    return closest, smallest

