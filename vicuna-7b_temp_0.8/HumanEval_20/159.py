from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest, largest = float('inf'), float('-inf')
    smallest_index = 0
    largest_index = len(numbers) - 1
    smallest_number = numbers[smallest_index]
    largest_number = numbers[largest_index]

    for index in range(1, len(numbers)):
        number = numbers[index]
        if number < smallest_number:
            smallest = smallest_number
            smallest_index = index
            smallest_number = number
        elif number > largest_number:
            largest = largest_number
            largest_index = index
            largest_number = number

    return smallest, largest

