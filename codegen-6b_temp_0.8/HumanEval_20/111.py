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
        raise ValueError("Length of numbers must be at least two")
    first_pair = (numbers[0], numbers[1])
    for i in range(0, len(numbers) - 1):
        are_close = numbers[i] == numbers[i + 1]
        if are_close:
            second_pair = (numbers[i], numbers[i + 1])
        if are_close and abs(first_pair[0] - first_pair[1]) > abs(second_pair[0] - second_pair[1]):
            first_pair = second_pair
    return first_pair

