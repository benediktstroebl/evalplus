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

    min_distance = float('inf')
    closest_pair = None
    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            diff = number - numbers[j]
            distance = diff ** 2
            if distance < min_distance:
                min_distance = distance
                closest_pair = (i, j)

    return min_distance < threshold

