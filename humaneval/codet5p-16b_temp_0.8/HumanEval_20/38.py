from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    assert isinstance(numbers, list), "Supplied argument should be a list"
    assert len(numbers) >= 2, "Supplied list should be at least 2 elements long"
    assert all(isinstance(number, float) for number in numbers), "List should contain only floats"
    return (min(numbers), max(numbers))
