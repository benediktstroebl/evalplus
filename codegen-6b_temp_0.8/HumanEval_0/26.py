from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    smallest = float('inf')
    i = 0
    while i < len(numbers):
        x = numbers[i]
        if x < smallest:
            smallest = x
        i = i + 1
    for j in range(i, len(numbers)):
        y = numbers[j]
        if smallest + threshold >= y >= smallest:
            return True

    return False

