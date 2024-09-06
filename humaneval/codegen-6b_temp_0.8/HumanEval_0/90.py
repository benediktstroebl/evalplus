from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # If the list is empty, then there are no close elements.
    if len(numbers) == 0:
        return False

    # If the list has only one number, then no close elements.
    if len(numbers) == 1:
        return False

    # Sort the list so that the check is simpler.
    numbers.sort()

    for index, number in enumerate(numbers):
        # Skip the first number.
        if index == 0:
            continue

        # Get the next index.
        next_index = index + 1

        # If the next number is more than threshold away from the current number, then we have
        # a close element.
        if abs(number - numbers[next_index]) > threshold:
            return True

    # No close elements were found.
    return False

