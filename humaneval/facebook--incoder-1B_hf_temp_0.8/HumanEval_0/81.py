from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers = list(map(float, numbers))

    length = len(numbers)
    if not length:
        return True

    delta = float(numbers[0] - numbers[1])
    count = 0
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i] - numbers[i + 1])
        if difference > delta:
            return False
        delta -= difference
        count += 1
        if count > threshold:
            return False

    return True

