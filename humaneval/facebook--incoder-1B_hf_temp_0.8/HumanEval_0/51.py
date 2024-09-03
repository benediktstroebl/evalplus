from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if not numbers:
        return False
    if len(numbers) == 1:
        return numbers[0] < threshold
    one_half = numbers[:1]
    two_half = numbers[1:]
    distances = [abs(one_half[i] - two_half[i]) for i in range(len(one_half))]
    half_count = len(half_count)
    if half_count > 0 and distances[0] < distances[1]:
        return True
    if half_count > 1 and distances[0] < distances[1]:
        return False
    return distances[0] < distances[1]

