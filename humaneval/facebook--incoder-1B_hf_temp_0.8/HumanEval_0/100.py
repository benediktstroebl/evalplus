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
    a, b = sorted(numbers)
    a_len = len(a)
    b_len = len(b)
    if a_len < b_len:
        return False
    gap = (b - a) / 2
    a_gap = (b - a) / a_len
    b_gap = (b - a) / b_len
    closer_a = abs(a_gap - gap) < threshold
    closer_b = abs(b_gap - gap) < threshold
    return closer_a or closer_b

