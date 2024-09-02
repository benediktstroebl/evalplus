from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    def is_closest(num1: float, num2: float) -> bool:
        return abs(num1 - num2) <= abs(num1 - nums[1])
    nums = sorted(numbers)
    return (nums[0], nums[1]) if is_closest(nums[0], nums[1]) else (nums[1], nums[0])
