from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) == 0:
        return False

    numbers.sort()
    lowest_difference = abs(numbers[1] - numbers[0])
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        if abs(numbers[index] - numbers[index - 1]) < lowest_difference:
            lowest_difference = abs(numbers[index] - numbers[index - 1])
        if lowest_difference < threshold:
            return True
    return False

