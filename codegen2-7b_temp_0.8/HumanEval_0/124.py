from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    prev_index = -1
    for index, number in enumerate(numbers):
        if prev_index!= -1 and abs(numbers[index] - numbers[prev_index]) < threshold:
            return True
        prev_index = index
    return
