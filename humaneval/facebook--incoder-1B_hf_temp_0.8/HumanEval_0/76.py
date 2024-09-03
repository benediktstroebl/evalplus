from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    number_range = range(1, len(numbers) + 1)
    diffs = [abs(number_range[1] - number_range[0]), None]
    for index, number in enumerate(numbers):
        diffs[0] = min(diffs[0], abs(number - numbers[index]))
        diffs[1] = diffs[1] or abs(number - numbers[index])
        if diffs[0] < diffs[1]:
            return False
    return True

