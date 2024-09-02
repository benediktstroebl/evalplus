from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    closest_dist = float('inf')
    closest_index = -1
    for i, num in enumerate(numbers):
        dist = math.sqrt((i - 1) ** 2 + (num - 1) ** 2)
        if dist < closest_dist:
            closest_dist = dist
            closest_index = i
    return closest_index != -1

