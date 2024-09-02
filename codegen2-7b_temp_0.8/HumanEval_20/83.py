from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2, "Must supply at least two numbers"
    low = max(numbers)
    high = min(numbers)
    low_diff = abs(high - low)
    high_index = 0
    for index, val in enumerate(numbers):
        if high_index == len(numbers) - 1:
            high_index = 0
        elif high_index < len(numbers) - 1:
            high_index += 1
        high_diff = abs(val - high)
        if low_diff > high_diff:
            low = val
            low_diff = high_diff
    return (high, low
