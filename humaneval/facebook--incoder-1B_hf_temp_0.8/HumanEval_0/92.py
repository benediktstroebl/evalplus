from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    thresholds = [threshold, threshold - 0.01, threshold - 0.01]
    for threshold in thresholds:
        if len(numbers) <= 2:
            return False

        number = numbers[0]
        other_numbers = numbers[1:]

        if len(other_numbers) <= 2:
            return True

        if number > other_numbers[0]:
            continue

        if other_numbers[0] > number > other_numbers[-1]:
            continue

        if len(numbers) == 1:
            return True

        difference = abs(number - other_numbers[0])
        if difference < threshold:
            continue

        return False

    return True

