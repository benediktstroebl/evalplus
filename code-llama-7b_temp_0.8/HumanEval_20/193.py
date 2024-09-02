from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2, "Can't have less than two numbers to compare!"

    smallest_pair: Tuple[float, float] = (float("inf"), float("inf"))
    for index in range(len(numbers)):
        if numbers[index] < numbers[index + 1]:
            smallest_pair = numbers[index], numbers[index + 1]
        else:
            smallest_pair = numbers[index + 1], numbers[index]
    return smallest_pair

