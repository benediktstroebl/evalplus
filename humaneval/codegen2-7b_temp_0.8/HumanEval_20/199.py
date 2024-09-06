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
        return None

    smaller_index, smaller_distance = -1, float("inf")
    larger_index, larger_distance = -1, float("inf")
    for i, number in enumerate(numbers):
        if number < smaller_distance:
            smaller_index = i
            smaller_distance = number
        if number > larger_distance:
            larger_index = i
            larger_distance = number
    return (numbers[smaller_index], numbers[larger_index]) if smaller_distance > larger_distance else (
        numbers[larger_index], numbers[smaller_index])



