from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2

    idx_smaller: int = 0
    smaller_number: float = numbers[0]
    for idx in range(1, len(numbers)):
        if numbers[idx] < smaller_number:
            smaller_number = numbers[idx]
            idx_smaller = idx
    idx_larger: int = idx_smaller + 1
    larger_number: float = numbers[idx_smaller]
    return (smaller_number, larger_number)

