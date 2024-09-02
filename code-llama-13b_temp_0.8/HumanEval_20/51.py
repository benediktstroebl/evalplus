from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    closest: Tuple[float, float] = (numbers[0], numbers[0])
    min_diff: float = float('inf')

    for idx, number in enumerate(numbers):
        if idx == 0:
            continue
        if number - numbers[idx - 1] < min_diff:
            closest = (numbers[idx - 1], number)
            min_diff = number - numbers[idx - 1]

    return closest

