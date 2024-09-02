from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    closest_dist = float("inf")
    for num1 in numbers:
        for num2 in numbers:
            distance = float("inf")
            for i in range(num1, num2 + 1):
                distance = min(distance, (num1 - i) ** 2 + (i - num2) ** 2)
            if distance < closest_dist:
                closest_dist = distance
    return closest_dist < threshold

