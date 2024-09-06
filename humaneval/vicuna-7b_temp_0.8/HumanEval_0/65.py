from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    closest_distance = float('inf')
    for i in range(len(numbers) - 1):
        distance = float("sqrt((numbers[i] - numbers[i+1])**2 + (numbers[i+1] - numbers[i])**2)")
        if distance < threshold:
            return False
        elif distance == threshold:
            return True
        else:
            closest_distance = distance
    return False

