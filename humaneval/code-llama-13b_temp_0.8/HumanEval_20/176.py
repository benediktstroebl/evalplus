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
    index_of_smallest_difference = 0
    smallest_difference = numbers[1] - numbers[0]
    for index in range(1, len(numbers) - 1):
        difference = numbers[index] - numbers[index - 1]
        if difference < smallest_difference:
            smallest_difference = difference
            index_of_smallest_difference = index
    return numbers[index_of_smallest_difference - 1], numbers[index_of_smallest_difference]

