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

    # get all numbers in pairs
    pairs = [
        (n1, n2)
        for n1, n2 in zip(numbers, numbers[1:])
        if abs(n1 - n2) <= threshold
    ]
    return len(pairs) > 0
