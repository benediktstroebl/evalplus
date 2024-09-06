from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    number_map = {}
    for number in numbers:
        number_map[number] = False

    for i, first in enumerate(numbers[:-1]):
        for j, second in enumerate(numbers[i + 1 :]):
            distance = abs(second - first)
            if distance > threshold:
                return True
            elif distance < threshold:
                number_map[second] = True

    return False

