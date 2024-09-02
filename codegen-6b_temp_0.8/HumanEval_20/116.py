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
        raise ValueError("Selected list of numbers must have at least two elements")
    a: float
    b: float
    min_difference: float
    a, b, min_difference = (
        numbers[0],
        numbers[1],
        abs(numbers[0] - numbers[1]),
    )
    for a, b in zip(numbers[:-1], numbers[1:]):
        difference = abs(a - b)
        if difference < min_difference:
            min_difference = difference
            a, b = a, b
    return a, b

