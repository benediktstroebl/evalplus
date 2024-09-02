from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_index = 0
    smallest_number = numbers[smallest_index]
    largest_index = 0
    largest_number = numbers[largest_index]
    for i in range(1, len(numbers)):
        if numbers[i] < smallest_number:
            smallest_index = i
            smallest_number = numbers[smallest_index]
        elif numbers[i] > largest_number:
            largest_index = i
            largest_number = numbers[largest_index]
    return smallest_number, largest_number

