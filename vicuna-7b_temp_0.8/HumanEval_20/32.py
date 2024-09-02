from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # If there are only two numbers, return them in order.
    if len(numbers) < 3:
        return numbers[0], numbers[1]

    # If there are three or more numbers, find the two closest to each other.
    smallest, second_smallest, largest = numbers
    third_smallest = numbers[0]
    third_smallest_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < third_smallest:
            smallest, third_smallest = third_smallest, numbers[i]
            third_smallest_index = i

    for i in range(1, len(numbers)):
        if numbers[i] < second_smallest:
            second_smallest = numbers[i]

    return smallest, second_smallest

