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
        raise ValueError("need at least 2 elements")

    # Sort the list
    numbers = sorted(numbers)

    if len(numbers) % 2 == 1:
        # There is an odd number of items in the list
        return min(numbers), max(numbers)

    # Even number of items in the list
    # Find the midpoint
    midpoint = len(numbers) // 2

    # Smallest difference
    diff_1 = abs(numbers[midpoint] - numbers[midpoint - 1])
    # Largest difference
    diff_2 = abs(numbers[midpoint] - numbers[midpoint + 1])

    if diff_1 == diff_2:
        # We have two equal differences
        return numbers[midpoint - 1], numbers[midpoint]
    if diff_1 > diff_2:
        # We have a higher difference
        return numbers[midpoint], numbers[midpoint + 1]
    else:
        # We have a higher difference
        return numbers[midpoint - 1], numbers[midpoint]

