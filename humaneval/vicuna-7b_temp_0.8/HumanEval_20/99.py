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
        return None, None

    smallest = numbers[0]
    largest = numbers[-1]
    first_middle = smallest - (largest - smallest) / 2
    second_middle = numbers[1] - first_middle

    smallest_diff = smallest - first_middle
    largest_diff = largest - first_middle
    if smallest_diff < largest_diff:
        smallest = first_middle
        largest = smallest + largest_diff
    else:
        smallest = first_middle
        largest = smallest + smallest_diff

    return smallest, largest