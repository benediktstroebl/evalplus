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

    pivot = len(numbers) // 2
    if pivot == 0:
        pivot = 1

    num_1 = numbers[pivot]
    num_2 = num_1
    for i in range(pivot, len(numbers) - 1):
        num_2 = numbers[i]
        if abs(num_1 - num_2) < threshold:
            return True
        num_1 = num_2

    return False

