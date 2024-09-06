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
        raise ValueError("At least two numbers required.")
    closest_elements: Tuple[float, float] = (numbers[0], numbers[1])
    for index in range(2, len(numbers)):
        if abs(numbers[index] - numbers[index - 1]) <= abs(numbers[index - 1] - numbers[index - 2]):
            closest_elements = (numbers[index - 1], numbers[index])
        else:
            closest_elements = (numbers[index - 2], numbers[index - 1])
    return closest_elements
