from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # assert len(numbers) >= 2
    # assert all(isinstance(i, float) for i in numbers)
    assert len(numbers) >= 2

    numbers.sort()
    largest = numbers[-1]
    try:
        minimal = numbers[numbers.index(largest) - 1]
    except ValueError:
        minimal = None
    return largest, minimal

