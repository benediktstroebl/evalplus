from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2:
        return False
    min_dist = 0.0
    min_distance = float('inf')
    for i in range(1, len(numbers)):
        for j in range(i):
            dist = (numbers[i] - numbers[j])
            distance = dist ** 2
            if distance < min_dist:
                min_dist = distance
                min_distance = dist
    return min_distance < threshold

