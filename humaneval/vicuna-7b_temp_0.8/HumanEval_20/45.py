from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest = numbers[0]
    largest = numbers[-1]
    for i in range(1, len(numbers)):
        smallest_i = smallest
        largest_i = largest
        for j in range(i, len(numbers)):
            delta = numbers[i] - numbers[j]
            if delta <= 0.0:
                smallest_i = smallest_i - delta
            elif delta > largest_i - smallest_i:
                smallest_i = smallest_i + delta
            largest_i = largest_i - delta
        smallest, largest = largest_i, smallest_i
    return smallest, largest