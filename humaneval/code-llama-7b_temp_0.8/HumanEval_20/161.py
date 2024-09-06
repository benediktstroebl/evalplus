from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Find the difference between the largest number and the smallest number in the list
    max_min_difference = max(numbers) - min(numbers)

    # Find the first two items in the list that are closest to each other.
    for i, item in enumerate(numbers):
        for item2 in numbers[i + 1:]:
            if abs(item - item2) < max_min_difference:
                closest_numbers = sorted((item, item2))
                return closest_numbers[0], closest_numbers[1]

