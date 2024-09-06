from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    for index1, number1 in enumerate(numbers):
        for index2, number2 in enumerate(numbers):
            if (
                index1 != index2
                and abs(number1 - number2) < threshold
                and (max(number1, number2), min(number1, number2))
                not in numbers[index1 + 1 :]
            ):
                return True
    return False

