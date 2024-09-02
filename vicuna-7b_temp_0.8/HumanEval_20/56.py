from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest, smallest_diff = float('inf'), float('inf')
    largest, largest_diff = float('-inf'), float('-inf')

    for n in numbers:
        smallest = min(smallest, n)
        smallest_diff = min(smallest_diff, abs(n - smallest))
        largest = max(largest, n)
        largest_diff = max(largest_diff, abs(n - largest))

    closest_num1 = smallest
    closest_num2 = largest

    return closest_num1, closest_num2