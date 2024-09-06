from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    numbers_length = len(numbers)
    if numbers_length <= 1:
        return False

    for index_1 in range(numbers_length):
        for index_2 in range(index_1 + 1, numbers_length):
            if abs(numbers[index_1] - numbers[index_2]) <= threshold:
                return True

    return False

