from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) == 2:
        return numbers[0], numbers[1]

    small, large = sorted([min(numbers), max(numbers)])

    small_diff, large_diff = abs(small - large), abs(large - small)
    return small if small_diff < large_diff else large, small if small_diff > large_diff else large

