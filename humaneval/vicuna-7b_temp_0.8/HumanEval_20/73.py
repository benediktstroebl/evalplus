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
        raise ValueError("List of numbers must contain at least two numbers")

    smallest_dist, second_smallest_dist = float("inf"), float("inf")
    smallest_index = 0
    second_smallest_index = 0

    for i in range(len(numbers)):
        smallest_dist = min(smallest_dist, numbers[i] - numbers[smallest_index])
        second_smallest_dist = min(second_smallest_dist, numbers[i] - numbers[second_smallest_index])

        if smallest_dist < float("inf") and second_smallest_dist < float("inf"):
            smallest_index = i
            second_smallest_index = smallest_index

    return smallest_index, second_smallest_index

