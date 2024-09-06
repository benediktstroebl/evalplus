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

    for number in numbers:
        # Skip first number
        if number == numbers[0]:
            continue

        # Check every pair of numbers, e.g. [1, 3], [3, 4], ...
        for second_number in numbers[numbers.index(number) + 1 :]:
            if abs(number - second_number) <= threshold:
                return True

    return False

