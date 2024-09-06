from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) == 2:
        return numbers

    smallest = min(numbers)
    min_dist = float("inf")
    answer, answer_index = None, None

    for index, value in enumerate(numbers):
        if value != smallest and value < min_dist:
            min_dist = value
            answer = value
            answer_index = index

    return smallest, answer

