from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nums_sorted = sorted(numbers)
    closest = nums_sorted[1]
    closest_diff = abs(nums_sorted[0] - closest)
    for i in range(1, len(numbers)):
        if abs(nums_sorted[i] - nums_sorted[i - 1]) < closest_diff:
            closest = nums_sorted[i] if nums_sorted[i] != nums_sorted[i - 1] else nums_sorted[i - 1]
            closest_diff = abs(nums_sorted[i] - nums_sorted[i - 1])
    return min(closest, nums_sorted[0]), max(closest, nums_sorted[0])

