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
        return numbers[0], numbers[0]
    smallest, second_smallest = None, None
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            smallest = numbers[i]
            second_smallest = numbers[i - 1]
        else:
            if second_smallest is not None and smallest < second_smallest:
                smallest, second_smallest = second_smallest, smallest
    return smallest, second_
