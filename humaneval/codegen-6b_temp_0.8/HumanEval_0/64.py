from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers.sort()
    number = numbers[0]
    max_number_index = len(numbers) - 1
    for i, _ in enumerate(numbers[1:], start=1):
        if numbers[i] - number < threshold:
            return True
        else:
            number = numbers[i]
    return False

