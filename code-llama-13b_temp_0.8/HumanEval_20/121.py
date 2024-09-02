from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # sorting in ascending order
    numbers.sort()

    # getting the absolute difference
    differences = []
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        differences.append((diff, numbers[i], numbers[i + 1]))

    # getting the smallest difference
    smallest_diff = min(differences)

    return smallest_diff[1], smallest_diff[2]

