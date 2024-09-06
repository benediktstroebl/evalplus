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
        raise ValueError("Find closest requires a list of at least two elements")
    if len(numbers) == 2:
        return (numbers[0], numbers[1])
    sorted_numbers = sorted(numbers)
    index_1 = numbers.index(sorted_numbers[0])
    index_2 = numbers.index(sorted_numbers[1])
    if abs(index_1 - index_2) == 1:
        return (sorted_numbers[0], sorted_numbers[1])
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
    closest_1 = sorted_numbers[index_1]
    closest_2 = sorted_numbers[index_2]
    if abs(closest_1 - closest_2) < abs(sorted_numbers[-1] - sorted_numbers[-2]):
        return (closest_1, closest_2)
    return (closest_2, closest_1)


import pytest

TEST_CASES = [
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
    ([0.0], (0.0, 0.0)),
    ([-1.0, 0.0, 2.0], (-1.0, 2.0)),
    ([-1.0, 3.0, 2.0], (-1.0, 2.0)),
    ([-1.0, 3.0, 2.0], (2.0, -1.0)),
    ([0.0], (0.0, 0.0)),
    ([-1.0, 0.0, 2.0], (-1.0, 1.0)),
    ([-1.0, 0.0, 2.0], (1.5, -1.5)),
    ([-