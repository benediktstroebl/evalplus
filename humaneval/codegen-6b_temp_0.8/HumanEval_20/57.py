from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2, "list must have at least two elements"

    previous_difference = None
    i1, i2 = None, None
    for i in range(len(numbers)):
        difference = abs(numbers[i] - numbers[i - 1])
        if i1 is None or difference < previous_difference:
            i1 = i
            i2 = i - 1
            previous_difference = difference

    return numbers[i1], numbers[i2]

